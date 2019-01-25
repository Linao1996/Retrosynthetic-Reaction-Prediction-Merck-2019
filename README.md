# 一些比赛前期工作  探索性数据分析 论文 开源方案
https://github.com/yvquanli/Retrosynthetic-Reaction-Prediction-Merck-2019
# some ideas
先总结一下思路，把基本的框架搭起来。  
Smarts是扩展的smiles形式，  
smile parse  
先标准化后再tokenize  
赛题处理方法好像挺多的，听说有用graph NN的  
evaluation都写的不清不楚, 没有公式  
神经翻译/问答系统  的思想  
chemdraw可以识别反应语法
rules作为输入


# 分子特征提取
分子特征一般有两种，描述符和分子指纹。分子指纹就是单纯的基于官能团，只能体现分子的结构信息。分子描述符会计算分子的一些理化性质，分子描述符一般用dragon那个软件算。分子指纹的话有很多类型，也有很多的包可以实现。  dragon是一个软件，算的比较全。    
分子指纹的话有很多包，
- 如rdkit，openbabel ,其他计算分子指纹的，
- 有利用图卷积的方法，  
- 还有一种是基于自编码器的方法，  

相当于使用模型提特征  
smiles计算分子指纹比较容易，计算描述符还得转成mol或者其他格式

# Paper
__[seq2seq]__  
逆合成paper 他们是首先把生成物多余一个的方程式筛掉了，1product-->几个reactants。但是结果还是不怎么样，我们虽然这里加入了反应试剂，虽说信息量会增加，但不太清楚会不会干预预测  
__[NMT神经翻译]__
[Link](https://arxiv.org/pdf/1612.09529.pdf)  
借用神经翻译的思想，Translating 'reagents and reactants' to 'products'.

1. Philippe S , Theophile G , Lányi Dávid, et al. __“Found in Translation”: Predicting Outcomes of Complex Organic Chemistry Reactions using Neural Sequence-to-Sequence Models[J]__. Chemical Science, 2018:10.1039.C8SC02339E-.
2. Schwaller P , Laino T , Gaudin, Théophile, et al. __Molecular Transformer for Chemical Reaction Prediction and Uncertainty Estimation[J]__. 2018.
3. Javier L. Baylon, Nicholas A. Cilfone. etc.__Enhancing Retrosynthetic Reaction Prediction with Deep Learning using Multiscale Reaction Classification__. Journal of Chemical Information and Modeling. 2019.
4. Segler M H S , Waller M P . __Neural-Symbolic Machine Learning for Retrosynthesis and Reaction Prediction[J]__. Chemistry - A European Journal, 2017, 23(25):5966-5971.
5. Liu B , Ramsundar B , Kawthekar P , et al. __Retrosynthetic Reaction Prediction Using Neural Sequence-to-Sequence Models[J]__. ACS Central Science, 2017:acscentsci.7b00303.  
[Code](https://github.com/pandegroup/reaction_prediction_seq2seq)  
6. Nam J , Kim J . __Linking the Neural Machine Translation and the Prediction of Organic Chemistry Reactions[J]__. 2016.   
[Code](https://github.com/recisic/reaction-translation)  
7. Savage J, Kishimoto A, Buesser B, et al. __Chemical Reactant Recommendation Using a Network of Organic Chemistry[C]__// Eleventh Acm Conference. 2017.



# 解决方案源码
__[seq2seq]__ [Link](https://github.com/pandegroup/reaction_prediction_seq2seq)  
__[NMT神经翻译]__
[Link](https://github.com/recisic/reaction-translation)  
__[transformer]__
[Link](https://github.com/FilippNikitin/ReactionPrediction)   
带有一些smiles预处理代码 tokenize  
__[tensor2tensor]__  [Link](https://github.com/fendaq/Retrosynthetic-Reaction-Prediction )  
有人尝试使用tensor2tensor构建Transformer，来做，但是好像不了了之了， 

# 官方教程
[有机化学基础 Part 1](https://www.bilibili.com/video/av41298615)  
视频介绍了有机化学中的专有名词、相关化学键、化学反应方程式的知识。同时，对烷烃、烯烃、炔烃、苯和芳香烃的官能团、结构特征和化学反应进行了详细的介绍.  
[有机化学基础 Part 2](https://www.bilibili.com/video/av41298872)  
视频介绍了醇、酚、醛和酮、羧酸、酯类的官能团、结构特征和化学反应，并分析了几种典型有机合成反应及其案例  
[SMILES表达式培训](https://www.bilibili.com/video/av41453917)  
视频介绍了 SMILES 的相关知识  
[解题思路](https://www.bilibili.com/video/av41457463)  
视频介绍了 SMILES 的解题思路
# 一些文档 
从模型到代码全面解析Google Tensor2Tensor系统
https://segmentfault.com/a/1190000015575985  
完全图解RNN、RNN变体、Seq2Seq、Attention机制
https://zhuanlan.zhihu.com/p/28054589

# QA系统
seq2seq https://github.com/kevinwei30/tf-DeepQA





