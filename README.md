# [*IEEE VIS* 2024] LLaVA-Chart: Advancing Multimodal Large Language Models in Chart Question Answering with Visualization-Referenced Instruction Tuning
Paper Link: https://arxiv.org/abs/2407.20174
<img width="1429" alt="data-generation-pipeline" src="https://github.com/user-attachments/assets/b59bab9f-26ad-49f2-9197-2ab75d65af79">
## Release
* 🔥 A more well-organized version of the chart generation pipeline is now available in [this new repository](https://github.com/zengxingchen/ChartGeneration).
* We have released all the code and datasets used in our paper.
* The generated data and selected benchmark can be downloaded in the [huggingface link](https://huggingface.co/datasets/lewy666/ChartInstructionData).
* Our model weights are available at the [huggingface link](https://huggingface.co/lewy666/llava-hr-ChartInstruction/tree/main).
## To-dos
- [ ] Write a walk-through tutorial about this repo.

<details>
  <summary>Data Gallery</summary>
<img width="865" alt="chart-gallery-1" src="https://github.com/user-attachments/assets/b1f3a60c-6fcd-4b4d-9cf6-fa950997901f">
<img width="856" alt="chart-gallery-2" src="https://github.com/user-attachments/assets/f5fa541d-9741-412c-bdfb-2bc1a7a34555">

</details>

## Evaluation
You can run our evaluation bash scripts `scripts/*.sh`.


## CLI Inference
Here is the command for chatting with our model without the need for a Gradio interface.
```
python -m model/high_resolution/llava_hr.serve.cli \
    --model-path ./checkpoints/llava-hr-ChartInstruction \
    --image-file "*.jpg" 
```
## Usage and License Notices: 
* For the base model llava: This project utilizes certain datasets and checkpoints that are subject to their respective original licenses. Users must comply with all terms and conditions of these original licenses, including but not limited to the OpenAI Terms of Use for the dataset and the specific licenses for base language models for checkpoints trained using the dataset (e.g. Llama community license for LLaMA-2 and Vicuna-v1.5). 

## Acknowledgement
- [Vicuna](https://github.com/lm-sys/FastChat): the codebase LLaVA built upon. LLaVA's base language model is Vicuna-13B.
- [LLaVA](https://github.com/haotian-liu/LLaVA): the codebase we built upon. LLaVA was the only open-sourced project with all training code open-sourced when we started this work.
- [LLaVA-HR](https://github.com/luogen1996/LLaVA-HR): the high-resolution version model we built upon. 
- [SemDeDup](https://github.com/facebookresearch/SemDeDup): the sampling module we are based on. SemDeDup is designed for hundred million of image sampling.
- [WYTIWYR](https://github.com/SerendipitysX/WYTIWYR): Part of data our classification are collected from here.
- [Unichart](https://github.com/vis-nlp/UniChart): Part of existing data are first collected by Unichart.

## Contact
If you have any questions about this work, please email Xingchen Zeng at xingchen.zeng@outlook.com.

## Citation
```
@article{zeng2024vis,
  author={Zeng, Xingchen and Lin, Haichuan and Ye, Yilin and Zeng, Wei},
  journal={IEEE Transactions on Visualization and Computer Graphics}, 
  title={Advancing Multimodal Large Language Models in Chart Question Answering with Visualization-Referenced Instruction Tuning}, 
  year={2024},
  pages={1-11},
  doi={10.1109/TVCG.2024.3456159}
}
```

