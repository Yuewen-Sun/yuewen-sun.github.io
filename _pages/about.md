---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently a postdoctoral researcher at Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) and Carnegie Mellon University (CMU), supervised by Prof. Kun Zhang. I received my Ph.D. from Southeast University under the supervision of Prof. Changyin Sun.

My research interests include causal representation learning and reinforcement learning, with publications <a href='https://scholar.google.com/citations?hl=en&user=LboR1toAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> at top AI conferences such as NeurIPS, ICLR, and AAAI. My recent work focuses on multimodal causal representation learning and its applications in healthcare to address challenges in identifiability.


# 🔥 News
- *2024.12*: &nbsp;🎉 Two papers are accepted by NeurIPS'24. 
- *2024.05*: I gave an invited talk on DataFunSummit2024. 
- *2024.01*: &nbsp;🎉 One paper is accepted by AAAI'24. 
- *2023.04*: I started postdoctoral research at MBZUAI and CMU.
- *2022.08*: &nbsp;🎉 I am a top reviewer of UAI'22.


# 📝 First Author Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/imdp_neurips24.png' alt="sym" width="100%" ></div></div>
<div class='paper-box-text' markdown="1">

[Identifying Latent State-Transition Processes for Individualized RL](https://openreview.net/pdf?id=kREpCQtHdN)

**Yuewen Sun**, Biwei Huang, Yu Yao, Donghuo Zeng, Xinshuai Dong, Songyao Jin, Boyang Sun, Roberto Legaspi, Kazushi Ikeda, Peter Spirtes, Kun Zhang

[**Project**](https://openreview.net/forum?id=kREpCQtHdN&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DNeurIPS.cc%2F2024%2FConference%2FAuthors%23your-submissions)) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We aim to identify the latent state-transition processes from observed state-action trajectories, facilitating the learning of personalized RL policies.
- Theoretical identifiability is guaranteed under both finite and infinite latent factor conditions, supporting the framework’s robustness.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='images/acamda_aaai24.png' alt="sym" width="100%" ></div></div>
<div class='paper-box-text' markdown="1">

[ACAMDA: Improving Data Efficiency in Reinforcement Learning Through Guided Counterfactual Data Augmentation](https://ojs.aaai.org/index.php/AAAI/article/view/29442/30719)

**Yuewen Sun**, Erli Wang, Biwei Huang, Chaochao Lu, Lu Feng, Changyin Sun, Kun Zhang 

[**Project**](https://ojs.aaai.org/index.php/AAAI/article/view/29442) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We employ counterfactual reasoning to generate augmented datasets, enabling agents to make unbiased decisions, and model causal relationships within the system to ensure adaptability across heterogeneous environments.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2022</div><img src='images/leap_iclr22.png' alt="sym" width="100%" ></div></div>
<div class='paper-box-text' markdown="1">

[Learning Temporally Causal Latent Processes from General Temporal Data](https://arxiv.org/abs/2110.05428)

Weiran Yao<sup>\*</sup>, **Yuewen Sun<sup>\*</sup>**, Alex Ho, Changyin Sun, Kun Zhang (<sup>\*</sup>Equal contribution)

[**Project**](https://github.com/weirayao/leap) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose two provable conditions under which temporally causal latent processes can be identified from their observed nonlinear mixtures.
- We develop a theoretically-grounded training framework that enforces the assumed
conditions through proper constraints.

</div>
</div>

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

# 🎖 Honors and Awards
- *2022.08* Top reviewer of UAI'22.


# 💼 Experience
- *2023.04 - Now*, Postdoctoral Researcher, Department of Machine Learning, MBZUAI & CMU.
- *2021.02 - 2021.10* (Internship), NEC Laboratories, China. 


# 📖 Educations
- *2017.09 - 2023.03*, Ph.D. in Control Science and Engineering, Southeast University, China. 
- *2013.09 - 2017.06*, Bachelor of Control Science and Engineering, Shandong University, China.  
- *2013.09 - 2017.06*, Bachelor of Financial Mathematics and Financial Engineering, Shandong University, China.  


# 💬 Invited Talks
- *2024.05*, Causal Representation Learning: Theoretical Innovations and Practical Applications, DataFunSummit2024. 
<!-- - *2024.05*, Causal Representation Learning: Theoretical Innovations and Practical Applications, DataFunSummit2024. \| [\[video\]](https://github.com/) -->
