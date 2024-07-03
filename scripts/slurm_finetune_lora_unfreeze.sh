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

CKPT="llava-v1.5-13b-lora-ChartInstruct"
# CKPT="llava-v1.5-13b-lora-qa_chart2table-md-unfreeze-debugg"


ROOT_MODEL_PATH="./checkpoints/$CKPT"
DATA_PATH="playground/data/qa(chartqa)-unichart_qa325k.json"
IMAGE_FOLDER="playground/data"
# BASE_MODEL="models/llava-v1.6-vicuna-13b"
BASE_MODEL="models/llava-v1.5-13b"

export TRANSFORMERS_OFFLINE=1
export NCCL_SOCKET_IFNAME=lo
export WANDB_NAME=$CKPT

deepspeed llava/train/train_mem.py \
    --lora_enable True --lora_r 128 --lora_alpha 256 --mm_projector_lr 2e-5 \
    --deepspeed ./scripts/zero3.json \
    --model_name_or_path $BASE_MODEL\
    --version v1 \
    --data_path  $DATA_PATH \
    --image_folder  $IMAGE_FOLDER \
    --vision_tower openai/clip-vit-large-patch14-336 \
    --mm_projector_type mlp2x_gelu \
    --mm_vision_select_layer -2 \
    --mm_use_im_start_end False \
    --mm_use_im_patch_token False \
    --image_aspect_ratio pad \
    --group_by_modality_length True \
    --bf16 True \
    --output_dir $ROOT_MODEL_PATH \
    --num_train_epochs 3 \
    --per_device_train_batch_size 16 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "epoch" \
    --save_total_limit 10 \
    --learning_rate 2e-4 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --dataloader_num_workers 4 \
    --lazy_preprocess True \
    --report_to wandb\

bash ~/projects/LLaVA/our_scripts/eval_finetune_lora.sh $BASE_MODEL $CKPT