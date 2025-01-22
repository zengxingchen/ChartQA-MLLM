#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p i64m1tga800u
#SBATCH -J pytorch
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task 64
#SBATCH --gres=gpu:8
#SBATCH --qos=high

module load pdsh-2.29
srun hostname -s > hostfile.txt
export TRANSFORMERS_OFFLINE=1
source ~/anaconda3/bin/activate llava-hr
cd ~/ChartQA-MLLM


export GPUS_PER_NODE=8
export MASTER_ADDR=$(scontrol show hostnames $SLURM_JOB_NODELIST | head -n 1)
export MASTER_PORT=9901

slots_per_node=8

# create new hostfile
rm hostfile.txt 
touch hostfile.txt

# get the name of each node and add slots info
for node in $(scontrol show hostnames $SLURM_JOB_NODELIST); do
  echo "$node slots=$slots_per_node" >> hostfile.txt
done
export WANDB_NAME=llava-hr-x-13b-chart

DATA_PATH='./playground/data/llava665K_vis467K.json'


deepspeed --hostfile hostfile.txt --master_addr=$MASTER_ADDR  --master_port=$MASTER_PORT model.llava_hr/train/train_mem.py \
    --deepspeed ./scripts/zero3.json \
    --model_name_or_path ~/projects/LLaVA/models/vicuna-13b-v1.5\
    --version v1 \
    --data_path $DATA_PATH\
    --image_folder ~/projects/LLaVA/playground/data \
    --vision_tower openai/clip-vit-large-patch14-336 \
    --vision_tower_slow convnext_xxlarge.clip_laion2b_soup \
    --pretrain_mm_mlp_adapter models/llava-hr-13b-x-pretrain-384/mm_projector.bin \
    --mm_projector_type mlp2x_gelu \
    --mm_vision_select_layer -2 \
    --mm_use_im_start_end False \
    --mm_use_im_patch_token False \
    --image_aspect_ratio pad \
    --group_by_modality_length True \
    --bf16 True \
    --output_dir ./checkpoints/llava-hr-x-13b-sft-768-cqa-331 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 2000 \
    --save_total_limit 5 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2496 \
    --gradient_checkpointing True \
    --dataloader_num_workers 4 \
    --lazy_preprocess True \
    --report_to wandb \
    --is_multipath_encoder True \
    --freeze_vision False \
    --input_image_size 1024