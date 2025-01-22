#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p i64m1tga800u
#SBATCH -J pytorch
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task 64 
#SBATCH --gres=gpu:8
#SBATCH --qos=high


export TRANSFORMERS_OFFLINE=0
source ~/anaconda3/bin/activate llava-hr
cd ~/ChartQA-MLLM

export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
gpu_list="${CUDA_VISIBLE_DEVICES:-0}"
IFS=',' read -ra GPULIST <<< "$gpu_list"

CHUNKS=${#GPULIST[@]}
CKPT="llava-hr-ChartInstruction"
MODEL_PATH="checkpoints/${CKPT}"
mkdir -p ./playground/eval/chartqa/$CKPT

# Define an associative array to store different question files
declare -A QUESTION_FILES=(
    ["aug"]="./playground/data/chartqa/chartqa_test_aug.jsonl"
    ["human"]="./playground/data/chartqa/chartqa_test_human.jsonl"
)

# Function to run the evaluation for a given question file
run_evaluation() {
    local question_file_key=$1
    local question_file=${QUESTION_FILES[$question_file_key]}


    for IDX in $(seq 0 $((CHUNKS-1))); do
        CUDA_VISIBLE_DEVICES=${GPULIST[$IDX]} python  -m llava_hr.eval.model_vqa_loader_ChartQA \
            --model-path  $MODEL_PATH\
            --question-file $question_file \
            --image-folder ./playground/eval/chartqa/test/png \
            --answers-file ./playground/eval/chartqa/$CKPT/${CHUNKS}_${IDX}_${question_file_key}.jsonl \
            --num-chunks $CHUNKS \
            --chunk-idx $IDX \
            --temperature 0 \
            --conv-mode vicuna_v1 &
    done
    wait


    output_file=./playground/eval/chartqa/$CKPT/merge_${question_file_key}.jsonl
    # Clear out the output file if it exists.
    > "$output_file"

    # Loop through the indices and concatenate each file.
    for IDX in $(seq 0 $((CHUNKS-1))); do
        cat ./playground/eval/chartqa/$CKPT/${CHUNKS}_${IDX}_${question_file_key}.jsonl >> "$output_file"
        rm -f ./playground/eval/chartqa/$CKPT/${CHUNKS}_${IDX}_${question_file_key}.jsonl
    done

    # Evaluate and append to the metric file with a label indicating the test set
    metric_file=./playground/eval/chartqa/$CKPT/metric.txt

    # Append a header with the test set name
    echo -e "=========================\n Metrics for $question_file_key test set:" >> "$metric_file"
    python ./playground/eval/chartqa/eval_chartqa_relaxed_acc.py \
        --result-file $output_file \
    >> "$metric_file"
}

# Run the evaluation for both question files
for key in "${!QUESTION_FILES[@]}"; do
    run_evaluation "$key"
done
