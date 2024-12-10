#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p i64m1tga800u
#SBATCH -J pytorch
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task 64
#SBATCH --gres=gpu:8
#SBATCH --qos=high

export TRANSFORMERS_OFFLINE=1
source ~/anaconda3/bin/activate llava
cd ~/projects/LLaVA

# export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
gpu_list="${CUDA_VISIBLE_DEVICES:-0}"
IFS=',' read -ra GPULIST <<< "$gpu_list"

CHUNKS=${#GPULIST[@]}
CKPT="llava-v1.5-13b-lora-ChartInstruct"
MODEL_PATH="./checkpoints/$CKPT"
BASE_MODEL="models/llava-v1.5-13b"
# BASE_MODEL="models/llava-v1.6-vicuna-13b"
mkdir -p ./playground/eval/chartqa/$CKPT

# Define an associative array to store different question files
declare -A QUESTION_FILES=(
    ["test"]="~/projects/LLaVA/playground/data/chart2table/test.jsonl"
)

# Function to run the evaluation for a given question file
run_evaluation() {
    local question_file_key=$1
    local question_file=${QUESTION_FILES[$question_file_key]}

    # for lora model
    
    for IDX in $(seq 0 $((CHUNKS-1))); do
        CUDA_VISIBLE_DEVICES=${GPULIST[$IDX]} python ./llava/eval/model_vqa_chart2table.py \
            --model-path $MODEL_PATH  \
            --model-base $BASE_MODEL \
            --question-file $question_file \
            --image-folder ~/playground/data/chartqa/dataset/test/png \
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
}

# Run the evaluation for both question files
for key in "${!QUESTION_FILES[@]}"; do
    run_evaluation "$key"
done
