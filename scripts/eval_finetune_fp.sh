#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p i64m1tga800u
#SBATCH -J pytorch
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task 64 
#SBATCH --gres=gpu:8
#SBATCH --qos=high


source ~/anaconda3/bin/activate llava
cd ~/projects/LLaVA

gpu_list="${CUDA_VISIBLE_DEVICES:-0}"
IFS=',' read -ra GPULIST <<< "$gpu_list"
CHUNKS=${#GPULIST[@]}

CKPT=${1:-"llava-v1.5-13b-lora-ChartInstruct"}

mkdir -p ./playground/eval/chartqa/$CKPT

echo "Using checkpoint: $CKPT"
ROOT_MODEL_PATH="./checkpoints/$CKPT"

# 自动寻找含有"checkpoint"的子目录并放入数组
CHECKPOINTS=() # 包含原始检查点路径
while IFS=  read -r -d $'\0'; do
    CHECKPOINTS+=("$REPLY")
done < <(find "$ROOT_MODEL_PATH" -name "*checkpoint*" -type d -print0 | sort -z -t '-' -k3,3n)

for ckpt in "${CHECKPOINTS[@]}"; do
    echo "$ckpt"
done

# 确保eval目录存在


declare -A QUESTION_FILES=(
    ["aug"]="./playground/data/chartqa/chartqa_test_aug.jsonl"
    ["human"]="./playground/data/chartqa/chartqa_test_human.jsonl"
)

# declare -A QUESTION_FILES=(
#     ["aug"]="./playground/data/chartqa/chartqa_val_aug.jsonl"
#     ["human"]="./playground/data/chartqa/chartqa_val_human.jsonl"
# )

run_evaluation() {
    local question_file_key=$1
    local model_path=$2
    local question_file=${QUESTION_FILES[$question_file_key]}

    ckpt_name=$(basename "$model_path")

    for IDX in $(seq 0 $((CHUNKS-1))); do
        CUDA_VISIBLE_DEVICES=${GPULIST[$IDX]} python ./llava/eval/model_vqa_chartqa.py \
            --model-path $model_path  \
            --question-file $question_file \
            --image-folder ~/playground/data/chartqa/dataset/test/png \
            --answers-file ./playground/eval/chartqa/$CKPT/${ckpt_name}/${CHUNKS}_${IDX}_${question_file_key}.jsonl \
            --num-chunks $CHUNKS \
            --chunk-idx $IDX \
            --temperature 0 \
            --conv-mode vicuna_v1 &
    done
    wait

    output_file=./playground/eval/chartqa/$CKPT/${ckpt_name}/merge_${question_file_key}.jsonl
    # Clear out the output file if it exists.
    > "$output_file"

    for IDX in $(seq 0 $((CHUNKS-1))); do
        cat ./playground/eval/chartqa/$CKPT/${ckpt_name}/${CHUNKS}_${IDX}_${question_file_key}.jsonl >> "$output_file"
        rm -f ./playground/eval/chartqa/$CKPT/${ckpt_name}/${CHUNKS}_${IDX}_${question_file_key}.jsonl
    done

    metric_file=./playground/eval/chartqa/$CKPT/metric.txt
    echo -e "===========================\nMetrics for $question_file_key test set on $ckpt_name:" >> "$metric_file"
    python our_scripts/utils/eval_vqa_relaxed_acc.py \
        --result-file $output_file \
    >> "$metric_file"
}

# 对每个检查点和每个问题文件运行评估
for ckpt in "${CHECKPOINTS[@]}"; do
    for key in "${!QUESTION_FILES[@]}"; do
        run_evaluation "$key" "$ckpt"
    done
done