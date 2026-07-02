# 我的 GitHub Stars 分类汇总

> 一个按主题分类的 GitHub starred 仓库索引，覆盖具身智能 / 机器人 / VLA / SLAM / 感知 / 强化学习 / 时间序列 等 22 个方向。

**最近更新**：2026-07-02 · **仓库总数**：242 · **分类数**：22

## 为什么有这个仓库

GitHub Stars 的 Lists 功能目前**没有公开 API**（[社区讨论 #8293](https://github.com/orgs/community/discussions/8293)），无法脚本化批量管理。所以我把所有 starred 仓库按主题分类，做成一个 markdown 索引作为公开 README——既能在 GitHub 主页直接浏览，也能版本化、可搜索、可分享。

## 怎么用

- 按 `Ctrl+F` 搜索关键词（仓库全名 / 描述 / topic）
- 点击任意仓库名跳转到原仓库
- 顶部有目录，按分类跳转

## 分类概览

| # | 分类 | 数量 |
|---|---|---|
| 1 | 🤖 VLA & 具身智能基础模型 | 19 |
| 2 | 🦾 模仿学习 & 机械臂操作 / Teleoperation | 14 |
| 3 | 🦾 SO-ARM / SO-101 等低成本机械臂平台 | 4 |
| 4 | 🧍 人形机器人 (Humanoid) | 11 |
| 5 | 🐕 四足机器人 (Quadruped) | 11 |
| 6 | 🚶 Locomotion / 腿式运动学习 | 3 |
| 7 | 🎯 强化学习 (RL 算法 / Sim-to-Real / 课程) | 8 |
| 8 | 🧭 移动机器人导航 | 9 |
| 9 | 🛩️ 无人机 / UAV / Aerial Robotics | 12 |
| 10 | 🗺️ SLAM (Visual / LiDAR / RGBD) | 19 |
| 11 | 📡 VIO / GNSS / 多传感器融合 / 标定 | 19 |
| 12 | 📦 建图 / 3D 重建 / 体素 / 场图 | 8 |
| 13 | 🚗 自动驾驶 | 6 |
| 14 | 👀 感知 / 计算机视觉 | 22 |
| 15 | 🎮 仿真平台 / Simulators | 8 |
| 16 | 🌐 World Model & 序列模型 (SSM) | 7 |
| 17 | 🧰 机器人工具 / 库 / SDK | 13 |
| 18 | 🤖 ROS / 驱动 / 集成包 | 4 |
| 19 | 🧠 LLM / Agent / AI Coding 工具 | 10 |
| 20 | 📊 时间序列 / 金融预测 | 3 |
| 21 | 📚 学习资源 / 教程 / Awesome List | 30 |
| 22 | ❓ 其他 / 待分类 | 2 |

## 如何重新生成

```bash
# 1. 拉取 starred 仓库元数据
gh auth login  # 首次需要
gh api --paginate /users/zichnw/starred \
  --jq '. | to_entries[] | {full_name: .value.full_name, description: .value.description, topics: .value.topics, language: .value.language, url: .value.html_url}' \
  > stars_meta.jsonl

# 2. 修改 categorize.py 里的映射表（dict）按你的喜好调整分类

# 3. 运行生成 README
python3 categorize.py
```

映射表在 `categorize.py` 的 `M` 字典里，想改某仓库的分类直接改 dict 然后重跑即可。

---

## 目录

- [🤖 VLA & 具身智能基础模型 (Vision-Language-Action / Foundation Models)](#🤖-vla--具身智能基础模型-vision-language-action--foundation-models) — 19 项
- [🦾 模仿学习 & 机械臂操作 / Teleoperation](#🦾-模仿学习--机械臂操作--teleoperation) — 14 项
- [🦾 SO-ARM / SO-101 等低成本机械臂平台](#🦾-so-arm--so-101-等低成本机械臂平台) — 4 项
- [🧍 人形机器人 (Humanoid)](#🧍-人形机器人-humanoid) — 11 项
- [🐕 四足机器人 (Quadruped)](#🐕-四足机器人-quadruped) — 11 项
- [🚶 Locomotion / 腿式运动学习](#🚶-locomotion--腿式运动学习) — 3 项
- [🎯 强化学习 (RL 算法 / Sim-to-Real / 课程)](#🎯-强化学习-rl-算法--sim-to-real--课程) — 8 项
- [🧭 移动机器人导航](#🧭-移动机器人导航) — 9 项
- [🛩️ 无人机 / UAV / Aerial Robotics](#🛩️-无人机--uav--aerial-robotics) — 12 项
- [🗺️ SLAM (Visual / LiDAR / RGBD)](#🗺️-slam-visual--lidar--rgbd) — 19 项
- [📡 VIO / GNSS / 多传感器融合 / 标定](#📡-vio--gnss--多传感器融合--标定) — 19 项
- [📦 建图 / 3D 重建 / 体素 / 场图](#📦-建图--3d-重建--体素--场图) — 8 项
- [🚗 自动驾驶](#🚗-自动驾驶) — 6 项
- [👀 感知 / 计算机视觉 (检测/跟踪/姿态/光流)](#👀-感知--计算机视觉-检测跟踪姿态光流) — 22 项
- [🎮 仿真平台 / Simulators](#🎮-仿真平台--simulators) — 8 项
- [🌐 World Model & 序列模型 (SSM)](#🌐-world-model--序列模型-ssm) — 7 项
- [🧰 机器人工具 / 库 / SDK](#🧰-机器人工具--库--sdk) — 13 项
- [🤖 ROS / 驱动 / 集成包](#🤖-ros--驱动--集成包) — 4 项
- [🧠 LLM / Agent / AI Coding 工具](#🧠-llm--agent--ai-coding-工具) — 10 项
- [📊 时间序列 / 金融预测](#📊-时间序列--金融预测) — 3 项
- [📚 学习资源 / 教程 / Awesome List](#📚-学习资源--教程--awesome-list) — 30 项
- [❓ 其他 / 待分类](#❓-其他--待分类) — 2 项

## 🤖 VLA & 具身智能基础模型 (Vision-Language-Action / Foundation Models)
*(19 项)*

- **[allenai/molmoact2](https://github.com/allenai/molmoact2)** · `Python` — Official Repository for MolmoAct2
- **[allenzren/open-pi-zero](https://github.com/allenzren/open-pi-zero)** · `Python` — Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence
- **[dexmal/dexbotic](https://github.com/dexmal/dexbotic)** · `Python` — Dexbotic: Open-Source Vision-Language-Action Toolbox  `#codebase` `#cogact` `#memoryvla` `#openvla-oft` `#pi0` `#real-world` `#robotics` `#simulation` `#toolbox` `#vla` `#vln`
- **[FluxVLA/FluxVLA](https://github.com/FluxVLA/FluxVLA)** · `Python` — An all-in-one VLA engineering platform for embodied AI — from data to real-robot deployment.  `#embodiedai` `#real-robots` `#real-time` `#robotics` `#vision-language-action-model` `#vlm` `#world-action-model`
- **[gen-robot/RL4VLA](https://github.com/gen-robot/RL4VLA)** · `Python` — (无描述)
- **[huangwl18/VoxPoser](https://github.com/huangwl18/VoxPoser)** · `Python` — VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models  `#embodied-ai` `#foundation-models` `#large-language-models` `#motion-planning` `#robotic-manipulation` `#robotics` `#vision-language-model`
- **[NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T)** · `Python` — NVIDIA Isaac GR00T N1.7 -  A Foundation Model for Generalist Robots.
- **[NVlabs/cosmos-policy](https://github.com/NVlabs/cosmos-policy)** · `Python` — Cosmos Policy
- **[OpenDriveLab/UniVLA](https://github.com/OpenDriveLab/UniVLA)** · `Python` — [RSS 2025] Learning to Act Anywhere with Task-centric Latent Actions  `#robot-learning` `#vision-language-actions-models` `#vla`
- **[openvla/openvla](https://github.com/openvla/openvla)** · `Python` — OpenVLA: An open-source vision-language-action model for robotic manipulation.
- **[Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi)** · `Python` — (无描述)
- **[PRIME-RL/SimpleVLA-RL](https://github.com/PRIME-RL/SimpleVLA-RL)** · `Python` — [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning  `#reasoning` `#rl` `#vla`
- **[priyasundaresan/homer](https://github.com/priyasundaresan/homer)** · `Python` — (无描述)
- **[QwenLM/Qwen-RobotNav](https://github.com/QwenLM/Qwen-RobotNav)** · `—` — Official Repo for Qwen-RobotNav
- **[RLinf/LaWAM](https://github.com/RLinf/LaWAM)** · `Python` — (无描述)
- **[Robbyant/lingbot-va](https://github.com/Robbyant/lingbot-va)** · `Python` — [RSS 2026] Causal video-action world model for generalist robot control
- **[WM-PO/WMPO](https://github.com/WM-PO/WMPO)** · `Python` — Official Implementation of Paper: WMPO: World Model-based Policy Optimization for Vision-Language-Action Models
- **[wsakobe/TrackVLA](https://github.com/wsakobe/TrackVLA)** · `Python` — [CoRL 2025] Repository relating to "TrackVLA: Embodied Visual Tracking in the Wild"
- **[zst1406217/VR-Robo](https://github.com/zst1406217/VR-Robo)** · `Python` — [RA-L 2025] VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion

## 🦾 模仿学习 & 机械臂操作 / Teleoperation
*(14 项)*

- **[aCodeDog/legged-robots-manipulation](https://github.com/aCodeDog/legged-robots-manipulation)** · `Python` — (无描述)
- **[anubhav1772/6-dof-robotic-arm](https://github.com/anubhav1772/6-dof-robotic-arm)** · `C++` — 6 DOF Robotic Arm (ROS + Gazebo)  `#6dof` `#gazebo11` `#ikfast` `#moveit` `#octomap` `#robotic-arm` `#ros-noetic`
- **[huggingface/lerobot](https://github.com/huggingface/lerobot)** · `Python` — 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning
- **[husky/husky_manipulation](https://github.com/husky/husky_manipulation)** · `Shell` — Repository to store all necessary packages for common manipulator integrations
- **[lFatality/ros_moveit_gazebo_ws](https://github.com/lFatality/ros_moveit_gazebo_ws)** · `CMake` — A repo with an example how to use a manipulator URDF with moveIt and Gazebo
- **[MarkFzp/act-plus-plus](https://github.com/MarkFzp/act-plus-plus)** · `Python` — Imitation learning algorithms with Co-training for Mobile ALOHA: ACT, Diffusion Policy, VINN  `#imitation-learning` `#robotics`
- **[MarkFzp/mobile-aloha](https://github.com/MarkFzp/mobile-aloha)** · `Jupyter Notebook` — Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation  `#imitation-learning` `#robotics`
- **[Robotics-STAR-Lab/REMANI-Planner](https://github.com/Robotics-STAR-Lab/REMANI-Planner)** · `C++` — [ICRA'24] Real-time Whole-body Motion Planning for Mobile Manipulators Using Environment-adaptive Search and Spatial-temporal Optimization
- **[RoboTwin-Platform/RoboTwin](https://github.com/RoboTwin-Platform/RoboTwin)** · `Python` — RoboTwin 2.0 Offical Repo  `#benchmark` `#data-generator` `#embodied-ai` `#robotics`
- **[Tian-Nian/control_your_robot](https://github.com/Tian-Nian/control_your_robot)** · `Python` — this project provide a verity of code help you collect data from your robotic arm, have fun!
- **[tonyzhaozh/act](https://github.com/tonyzhaozh/act)** · `Python` — (无描述)
- **[tonyzhaozh/aloha](https://github.com/tonyzhaozh/aloha)** · `Python` — (无描述)
- **[tud-amr/m3p2i-aip](https://github.com/tud-amr/m3p2i-aip)** · `Python` — Code for the IEEE Robotics and Automation Letters paper titled "Multi-Modal MPPI and Active Inference for Reactive Task and Motion Planning"
- **[zhanghengsjtu/mobile_manipulator_ros_simulation](https://github.com/zhanghengsjtu/mobile_manipulator_ros_simulation)** · `CMake` — Mobile manipulator simulation. Including agv navigation + robotic arm moveit planning.

## 🦾 SO-ARM / SO-101 等低成本机械臂平台
*(4 项)*

- **[commanderfun/STS3215](https://github.com/commanderfun/STS3215)** · `Python` — A multi-part tutorial for controlling the Feetech STS3215 servo (12V-30kg or 7.4V-19kg torque model) with Python and a Waveshare Serial Bus Servo Driver Board.  `#feetech` `#robotics` `#servos` `#sts3215`
- **[legalaspro/so101-ros-physical-ai](https://github.com/legalaspro/so101-ros-physical-ai)** · `Python` — ROS 2 stack for SO-101 leader/follower: Feetech driver, bringup, teleop, MoveIt2, episode recording, Rerun, policy inference.
- **[MuammerBay/isaac_so_arm101](https://github.com/MuammerBay/isaac_so_arm101)** · `Python` — Isaac Lab external project for SO-ARM100/101 arm robot.  `#isaac-lab` `#isaac-sim` `#isaaclab` `#isaacsim` `#nvidia` `#omniverse` `#reinforcement-learning` `#robotics` `#so-100` `#so-101` `#so-arm100` `#so100` `#so101` `#soarm` `#soarm-101` `#soarm100`
- **[TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100)** · `—` — Standard Open Arm 100

## 🧍 人形机器人 (Humanoid)
*(11 项)*

- **[DAVIAN-Robotics/PHUMA](https://github.com/DAVIAN-Robotics/PHUMA)** · `Python` — Code for "PHUMA: Physically Reliable Humanoid Locomotion Dataset"  `#dataset` `#humanoid` `#locomotion` `#retargeting` `#robotics`
- **[HUST-3W/GMR_autoik](https://github.com/HUST-3W/GMR_autoik)** · `Python` — [arXiv 2025] GMR: General Motion Retargeting. Retarget human motions into diverse humanoid robots in real time on CPU. Add IK-CONFIG auto-generation function for humanoid robots.
- **[InternRobotics/HoST](https://github.com/InternRobotics/HoST)** · `Python` — [RSS 2025 Best Systems Paper Finalist] 💐Official implementation of "Learning Humanoid Standing-up Control across Diverse Postures"
- **[LeCAR-Lab/BFM-Zero](https://github.com/LeCAR-Lab/BFM-Zero)** · `Python` — BFM_Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning  `#humanoid` `#reinforcement-learning` `#sim2real` `#unsupervised-learning`
- **[limxdynamics/tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab)** · `Python` — External extenstion template based on Isaac Lab
- **[NVlabs/GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl)** · `Python` — Welcome to GR00T Whole-Body Control (WBC)! This is a unified platform for developing and deploying advanced humanoid controllers. This includes: Decoupled WBC models used in NVIDIA Isaac-Gr00t, Gr00t N1.5 and N1.6 and GEAR-SONIC
- **[Open-X-Humanoid/TienKung-Lab](https://github.com/Open-X-Humanoid/TienKung-Lab)** · `Python` — Tien Kung-Lab: Direct IsaacLab Workflow for Legged Robots  `#embodied-ai` `#humanoid-robot` `#isaaclab` `#isaacsim` `#reinforcement-learning` `#sim2sim` `#tienkung`
- **[Renforce-Dynamics/beyondAMP](https://github.com/Renforce-Dynamics/beyondAMP)** · `Python` — beyondAMP provides a unified pipeline to integrate Adversarial Motion Priors (AMP) into any IsaacLab robot setup, with minimal modifications and full compatibility with custom robot designs.  `#amp` `#animation` `#isaaclab` `#motion` `#reinforcement-learning` `#robotics`
- **[Roboparty/roboto_origin](https://github.com/Roboparty/roboto_origin)** · `Python` — Roboto_origin Fully Open-Source DIY Humanoid Robot/萝博头原型机全开源手搓级人形机器人
- **[YanjieZe/GMR](https://github.com/YanjieZe/GMR)** · `Python` — [ICRA 2026] GMR: General Motion Retargeting. Retarget human motions into diverse humanoid robots in real time on CPU. Retargeter for TWIST.
- **[zju3dv/GVHMR](https://github.com/zju3dv/GVHMR)** · `Jupyter Notebook` — Code for "GVHMR: World-Grounded Human Motion Recovery via Gravity-View Coordinates", Siggraph Asia 2024, TPAMI 2026

## 🐕 四足机器人 (Quadruped)
*(11 项)*

- **[ARCaD-Lab-UM/RF-MPC](https://github.com/ARCaD-Lab-UM/RF-MPC)** · `MATLAB` — Representation-Free Model Predictive Control for Dynamic Quadruped
- **[chvmp/champ](https://github.com/chvmp/champ)** · `C++` — MIT Cheetah I Implementation  `#gazebo` `#gazebo-ros` `#gazebo-simulator` `#legged-robotics` `#legged-robots` `#quadruped` `#quadruped-robot-gaits` `#quadruped-simulation` `#robotics` `#ros`
- **[felipemohr/IsaacLab-Quadruped-Tasks](https://github.com/felipemohr/IsaacLab-Quadruped-Tasks)** · `Python` — Quadruped Tasks extension based on Isaac Lab.
- **[Mehooz/vision4leg](https://github.com/Mehooz/vision4leg)** · `Python` — Toolkit for vision-guided quadrupedal locomotion research
- **[mike4192/spotMicro](https://github.com/mike4192/spotMicro)** · `C++` — Spot Micro Quadruped Project
- **[mit-biomimetics/Cheetah-Software](https://github.com/mit-biomimetics/Cheetah-Software)** · `C++` — (无描述)
- **[OpenQuadruped/spot_mini_mini](https://github.com/OpenQuadruped/spot_mini_mini)** · `C++` — Dynamics and Domain Randomized Gait Modulation with Bezier Curves for Sim-to-Real Legged Locomotion.  `#control` `#environment` `#gait` `#gym-environment` `#locomotion` `#machine-learning` `#open-source` `#openai-gym` `#openai-gym-environments` `#optimization` `#pybullet` `#quadruped` `#quadruped-robot` `#quadruped-robot-gaits` `#quadruped-robots` `#reinforcement-learning` `#ros` `#spot` `#terrain` `#walker`
- **[PetoiCamp/OpenCat-Quadruped-Robot](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot)** · `C++` — An open source quadruped robot pet framework for developing Boston Dynamics-style four-legged robots that are perfect for STEM, coding & robotics education, IoT robotics applications, AI-enhanced robotics application services, research, and DIY robotics kit development.  `#ai` `#arduino` `#block-coding` `#education` `#iot` `#legged-robot` `#quadruped` `#quadruped-robot-gaits` `#raspberry-pi` `#robot-cat` `#robot-dog` `#robot-kit` `#robot-pet` `#robotics` `#robotics-education` `#simulation` `#stem` `#visual-programming` `#walking`
- **[PMY9527/QUAD-MPC-SIM-HW](https://github.com/PMY9527/QUAD-MPC-SIM-HW)** · `C++` — Inspired by the book, this is a basic implementation of a sim & real tested Model Predictive Controller for Unitree A1 / Go1 based on the finite state machine framework of Unitree Guide.
- **[shaheenbharwani/sim2real-3d-printed-quadruped](https://github.com/shaheenbharwani/sim2real-3d-printed-quadruped)** · `Python` — Complete sim-to-real AI quadruped robot: Isaac Lab training → ROS2 → physical hardware
- **[silvery107/rl-mpc-locomotion](https://github.com/silvery107/rl-mpc-locomotion)** · `Python` — Deep RL for MPC control of Quadruped Robot Locomotion  `#isaac-gym` `#mpc` `#quadruped` `#reinforcement-learning` `#robotics`

## 🚶 Locomotion / 腿式运动学习
*(3 项)*

- **[chengxuxin/extreme-parkour](https://github.com/chengxuxin/extreme-parkour)** · `Python` — [ICRA 2024]: Train your parkour robot in less than 20 hours.
- **[lucidrains/locoformer](https://github.com/lucidrains/locoformer)** · `Python` — LocoFormer - Generalist Locomotion via Long-Context Adaptation  `#adaptation` `#artificial-intelligence` `#attention-mechanisms` `#cross-embodiment` `#deep-learning` `#locomotion` `#transformers`
- **[yang-zj1026/legged-loco](https://github.com/yang-zj1026/legged-loco)** · `Python` — Low-level locomotion policy training in Isaac Lab

## 🎯 强化学习 (RL 算法 / Sim-to-Real / 课程)
*(8 项)*

- **[abmoRobotics/RLRoverLab](https://github.com/abmoRobotics/RLRoverLab)** · `Python` — Rover and space-related reinforcement learning environments implemented for Isaac Sim and Isaac Lab.
- **[danijar/dreamerv3](https://github.com/danijar/dreamerv3)** · `Python` — Mastering Diverse Domains through World Models  `#artificial-intelligence` `#general` `#jax` `#minecraft` `#reinforcement-learning` `#world-models`
- **[eureka-research/DrEureka](https://github.com/eureka-research/DrEureka)** · `Python` — Official Repository for "DrEureka: Language Model Guided Sim-To-Real Transfer" (RSS 2024)
- **[HybridRobotics/whole_body_tracking](https://github.com/HybridRobotics/whole_body_tracking)** · `Python` — (无描述)
- **[leggedrobotics/rsl_rl](https://github.com/leggedrobotics/rsl_rl)** · `Python` — A fast and simple implementation of learning algorithms for robotics.
- **[NVlabs/COMPASS](https://github.com/NVlabs/COMPASS)** · `Python` — Cross-embOdiment Mobility Policy via ResiduAl RL and Skill Synthesis
- **[project-instinct/InstinctLab](https://github.com/project-instinct/InstinctLab)** · `Python` — (无描述)
- **[Tsinghua-MARS-Lab/StateTransformer](https://github.com/Tsinghua-MARS-Lab/StateTransformer)** · `Python` — (无描述)

## 🧭 移动机器人导航
*(9 项)*

- **[2473o/PCT_planner](https://github.com/2473o/PCT_planner)** · `C++` — 3D navigation based on point cloud tomography.
- **[81578823/3D_navigation_PCTplanner](https://github.com/81578823/3D_navigation_PCTplanner)** · `C++` — 3D navigation in the room and on the stairs
- **[amap-cvlab/ABot-Navigation](https://github.com/amap-cvlab/ABot-Navigation)** · `—` — (无描述)
- **[byangw/PCT_planner](https://github.com/byangw/PCT_planner)** · `C++` — 3D navigation based on point cloud tomography
- **[InternRobotics/InternNav](https://github.com/InternRobotics/InternNav)** · `Jupyter Notebook` — InternRobotics' open platform for building generalized navigation foundation models.  `#mllms` `#navigation` `#robotics` `#spatial-ai` `#spatial-intelligence` `#vision-language-action-model` `#vision-language-navigation` `#visual-navigation` `#vla` `#vlm`
- **[upasana099/Autonomous-Navigation-of-Mobile-Manipulator](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator)** · `—` — The project involves the design and simulation of a mobile robot that is capable of navigating through a complex simulated environment space and manipulating an object after reaching to the target place  `#cpp` `#gazebo` `#hector-slam` `#ros-noetic` `#rviz`
- **[Zhefan-Xu/NavRL](https://github.com/Zhefan-Xu/NavRL)** · `C++` — [IEEE RA-L'25] NavRL: Learning Safe Flight in Dynamic Environments (NVIDIA Isaac/Python/ROS1/ROS2)  `#collision-avoidance` `#embodied-ai` `#isaac-sim` `#nvidia-isaac` `#reinforcement-learning` `#robot-navigation` `#robotics` `#ros1-noetic` `#ros2-humble`
- **[ZJU-FAST-Lab/Terrestrial-Aerial-Navigation](https://github.com/ZJU-FAST-Lab/Terrestrial-Aerial-Navigation)** · `C++` — An autonomous navigation framework that brings complete autonomy to terrestrial-aerial bimodal vehicles (TABVs)
- **[zm0612/Hybrid_A_Star](https://github.com/zm0612/Hybrid_A_Star)** · `C++` — Hybrid A Star algorithm C++ implementation

## 🛩️ 无人机 / UAV / Aerial Robotics
*(12 项)*

- **[ARK-Electronics/ROS2_PX4_Offboard_Example](https://github.com/ARK-Electronics/ROS2_PX4_Offboard_Example)** · `Python` — Example of controlling PX4 Velocity Setpoints with ROS2 Teleop controls
- **[ethz-asl/mav_voxblox_planning](https://github.com/ethz-asl/mav_voxblox_planning)** · `Makefile` — MAV planning tools using voxblox as the map representation.
- **[HenryHuYu/DiffPhysDrone](https://github.com/HenryHuYu/DiffPhysDrone)** · `Cuda` — Published on Nature Machine Intelligence! The first real robot(quadrotor) based on differentiable physics training.  `#drone` `#end-to-end` `#reinforcement-learning` `#robotics`
- **[HKUST-Aerial-Robotics/EPSILON](https://github.com/HKUST-Aerial-Robotics/EPSILON)** · `C++` — (无描述)
- **[HKUST-Aerial-Robotics/FIESTA](https://github.com/HKUST-Aerial-Robotics/FIESTA)** · `C++` — Fast Incremental Euclidean Distance Fields for Online Motion Planning of Aerial Robots  `#euclidean-distances` `#mapping` `#planning` `#robotics`
- **[HKUST-Aerial-Robotics/Teach-Repeat-Replan](https://github.com/HKUST-Aerial-Robotics/Teach-Repeat-Replan)** · `C++` — Teach-Repeat-Replan: A Complete and Robust System for Aggressive Flight in Complex Environments  `#aerial-robotics` `#autonomous-drone-race` `#autonomous-navigation` `#motion-planning` `#perception` `#uav`
- **[monemati/PX4-ROS2-Gazebo-YOLOv8](https://github.com/monemati/PX4-ROS2-Gazebo-YOLOv8)** · `Python` — Aerial Object Detection using a Drone with PX4 Autopilot and ROS 2. PX4 SITL and Gazebo Garden used for Simulation. YOLOv8 used for Object Detection.  `#docker` `#dockerfile` `#drone` `#gazebo` `#gz` `#gz-garden` `#gz-harmonic` `#object-detection` `#px4` `#px4-autopilot` `#px4-ros2-gazebo` `#pygame` `#ros` `#ros2` `#ros2-humble` `#simulation` `#sitl` `#uav` `#yolo` `#yolov8`
- **[rongbohou/px4_fast_planner](https://github.com/rongbohou/px4_fast_planner)** · `Python` — (无描述)
- **[SJTU-ViSYS-team/Avoid-MPC](https://github.com/SJTU-ViSYS-team/Avoid-MPC)** · `C++` — Mapless Collision-Free Flight via MPC using Dual KD-Trees in Cluttered Environments(IROS 2025)
- **[ZJU-FAST-Lab/ego-planner](https://github.com/ZJU-FAST-Lab/ego-planner)** · `C++` — (无描述)
- **[ZJU-FAST-Lab/ego-planner-swarm](https://github.com/ZJU-FAST-Lab/ego-planner-swarm)** · `C++` — An efficient single/multi-agent trajectory planner for multicopters.
- **[ZJU-FAST-Lab/EVA-planner](https://github.com/ZJU-FAST-Lab/EVA-planner)** · `C++` — EVA-planner: an EnVironmental Adaptive Gradient-based Local Planner for Quadrotors.  `#adaptive` `#planning` `#robotics`

## 🗺️ SLAM (Visual / LiDAR / RGBD)
*(19 项)*

- **[Cc19245/LVI-SAM-Easyused](https://github.com/Cc19245/LVI-SAM-Easyused)** · `C++` — LVI-SAM for easier using (更简单的使用LVI-SAM的方法)
- **[cpymaple/ORB-SLAM3-YOLOv3](https://github.com/cpymaple/ORB-SLAM3-YOLOv3)** · `C++` — (无描述)
- **[dachengxiaocheng/NDT-Transformer](https://github.com/dachengxiaocheng/NDT-Transformer)** · `Python` — This github is a supplementary material including data, code, trained model and demo for the paper "NDT-Transformer: Large-Scale 3D Point Cloud Localisation using the Normal Distribution Transform Representation".
- **[EndlessLoops/ORB_SLAM3_ROS2](https://github.com/EndlessLoops/ORB_SLAM3_ROS2)** · `C++` — ROS2 wrapping package for orbslam3 library
- **[Ewenwan/ORB_SLAM2_SSD_Semantic](https://github.com/Ewenwan/ORB_SLAM2_SSD_Semantic)** · `C++` — 动态语义SLAM 目标检测+VSLAM+光流/多视角几何动态物体检测+octomap地图+目标数据库  `#dynamic-slam` `#object-detection` `#octomap` `#semantic-slam`
- **[Factor-Robotics/Roller-Coaster-SLAM-Dataset](https://github.com/Factor-Robotics/Roller-Coaster-SLAM-Dataset)** · `—` — The world's first roller coaster SLAM dataset  `#dataset` `#localization` `#mapping` `#perception` `#robotics` `#roller-coaster` `#slam`
- **[HKUST-Aerial-Robotics/VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion)** · `C++` — An optimization-based multi-sensor state estimator
- **[introlab/rtabmap](https://github.com/introlab/rtabmap)** · `C++` — RTAB-Map library and standalone application  `#android` `#ios` `#localization` `#mapping` `#project-tango` `#robotics` `#ros` `#ros2` `#scanning` `#slam`
- **[JingwenWang95/DSP-SLAM](https://github.com/JingwenWang95/DSP-SLAM)** · `C++` — [3DV 2021] DSP-SLAM: Object Oriented SLAM with Deep Shape Priors  `#3d-reconstruction` `#kitti-dataset` `#lidar` `#object-slam` `#semantic-slam` `#slam`
- **[JokerJohn/LIO_SAM_6AXIS](https://github.com/JokerJohn/LIO_SAM_6AXIS)** · `C++` — LIO_SAM for 6-axis IMU and  GNSS.  `#6-axis-imu` `#gps` `#gtsam` `#lidar` `#lidar-inertial` `#lidarslam` `#lio` `#liosam` `#loam-velodyne` `#slam`
- **[LeonardoDiCaprio1/Map_ORBSLAM_ROS](https://github.com/LeonardoDiCaprio1/Map_ORBSLAM_ROS)** · `C++` — You can densely map datasets through RVIZ and create your own TUM dataset to create maps
- **[lturing/ORB_SLAM3_FAST_IMU_INIT](https://github.com/lturing/ORB_SLAM3_FAST_IMU_INIT)** · `C++` — (无描述)
- **[ov2slam/ov2slam](https://github.com/ov2slam/ov2slam)** · `C++` — OV²SLAM is a Fully Online and Versatile Visual SLAM for Real-Time Applications  `#bundle-adjustment` `#localization` `#opencv` `#ov2slam` `#real-time` `#slam` `#versatile` `#visison` `#visual-slam`
- **[SlamMate/CDS-SLAM-Semantic-mapping-in-dynamic-environment](https://github.com/SlamMate/CDS-SLAM-Semantic-mapping-in-dynamic-environment)** · `C++` — This project is the result of my undergraduate dissertation. The localization in dynamic environment is to deploy TensorRT optimized YOLOX in the front end of ORB-SLAM3 for object detection, and then eliminate all points belonging to the human bounding box. At the same time, the semantic information is sent to the mapping module to dye the 3D point cloud. The disadvantage of this project is that in the localization  module, only the points belonging to people are processed, because people are dynamic most of the time. In the mapping module, we did not segment semantic objects accurately, resulting in wrong coloring of point clouds of other objects.
- **[TixiaoShan/LVI-SAM](https://github.com/TixiaoShan/LVI-SAM)** · `C++` — LVI-SAM: Tightly-coupled Lidar-Visual-Inertial Odometry via Smoothing and Mapping  `#lidar-odometry` `#visual-odometry`
- **[UZ-SLAMLab/ORB_SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)** · `C++` — ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM  `#slam-algorithms`
- **[zang09/ORB-SLAM3-STEREO-FIXED](https://github.com/zang09/ORB-SLAM3-STEREO-FIXED)** · `C++` — Fixed version of ORB-SLAM3 stereo mode
- **[zang09/ORB_SLAM3_ROS2](https://github.com/zang09/ORB_SLAM3_ROS2)** · `C++` — ROS2 wrapping package for orbslam3 library
- **[zinuok/VINS-Fusion-ROS2](https://github.com/zinuok/VINS-Fusion-ROS2)** · `C++` — ROS2 version of VINS-Fusion

## 📡 VIO / GNSS / 多传感器融合 / 标定
*(19 项)*

- **[aau-cns/insane_dataset_tools](https://github.com/aau-cns/insane_dataset_tools)** · `MATLAB` — Tools to process data from the INSANE data set  `#datasets` `#mapping` `#robotics` `#sensor-data` `#sensor-fusion` `#uav`
- **[boxuLibrary/drt-vio-init](https://github.com/boxuLibrary/drt-vio-init)** · `C++` — The official repository of our CVPR2023 paper "A Rotation-Translation-Decoupled Solution for Robust and Efficient Visual-Inertial Initialization".
- **[CruxDevStuff/allan_ros2](https://github.com/CruxDevStuff/allan_ros2)** · `C++` — ROS2 package for analysing IMU noise parameters using allan deviation plots. Based on Kalibr IMU noise model  `#calibration` `#imu-calibration` `#imu-sensor`
- **[dzunigan/imu_initialization](https://github.com/dzunigan/imu_initialization)** · `C++` — Implementation of "An Analytical Solution to the IMU Initialization Problem for Visual-Inertial Systems"
- **[ethz-asl/kalibr](https://github.com/ethz-asl/kalibr)** · `C++` — The Kalibr visual-inertial calibration toolbox  `#calibration` `#calibration-toolbox` `#camera` `#imu`
- **[HKUST-Aerial-Robotics/gnss_comm](https://github.com/HKUST-Aerial-Robotics/gnss_comm)** · `C++` — Basic definitions and utility functions for GNSS raw measurement processing  `#gnss` `#ros`
- **[HKUST-Aerial-Robotics/GVINS](https://github.com/HKUST-Aerial-Robotics/GVINS)** · `C++` — Tightly coupled GNSS-Visual-Inertial system for locally smooth and globally consistent state estimation in complex environment.  `#estimation-algorithm` `#gnss` `#localization` `#sensor-fusion` `#slam`
- **[HKUST-Aerial-Robotics/GVINS-Dataset](https://github.com/HKUST-Aerial-Robotics/GVINS-Dataset)** · `C++` — A dataset containing synchronized visual, inertial and GNSS raw measurements.  `#dataset` `#gnss` `#gnsstoolkit` `#imu` `#stereo-camera`
- **[i2Nav-WHU/IC-GVINS](https://github.com/i2Nav-WHU/IC-GVINS)** · `C++` — A Robust, Real-time, INS-Centric GNSS-Visual-Inertial Navigation System  `#slam` `#vins` `#vio`
- **[i2Nav-WHU/OB_GINS](https://github.com/i2Nav-WHU/OB_GINS)** · `C++` — An Optimization-Based GNSS/INS Integrated Navigation System  `#gins` `#slam`
- **[JiangboSong251/R2-GVIO](https://github.com/JiangboSong251/R2-GVIO)** · `—` — A Robust, Real-Time GNSS-Visual-Inertial State Estimator in Urban Challenging Environments
- **[SJTU-ViSYS/M2DGR](https://github.com/SJTU-ViSYS/M2DGR)** · `—` — M2DGR： a Multi-modal and Multi-scenario Dataset for Ground Robots(RA-L2021 & ICRA2022)  `#dataset` `#robotics` `#slam`
- **[symao/vio_evaluation](https://github.com/symao/vio_evaluation)** · `Python` — Compare state-of-the-art VO/VSLAM/VIO packages in EuRoC datasets. Algorithms include VINS, MSCKF, ORB-SLAM, SVO2 etc.  `#vio` `#vslam`
- **[tomojitakasu/RTKLIB](https://github.com/tomojitakasu/RTKLIB)** · `C` — (无描述)
- **[UCR-Robotics/Citrus-Farm-Dataset](https://github.com/UCR-Robotics/Citrus-Farm-Dataset)** · `Python` — IROS/ISVC 2023: Multimodal Dataset for Localization, Mapping and Crop Monitoring in Citrus Tree Farms  `#agricultural-robotics` `#agriculture` `#citrus` `#citrus-farm` `#dataset` `#datasets` `#isvc` `#localization` `#mapping` `#multimodal` `#odometry` `#robotics` `#slam`
- **[weisongwen/UrbanLoco](https://github.com/weisongwen/UrbanLoco)** · `Python` — UrbanLoco: A Full Sensor Suite Dataset for Mapping and Localization in Urban Scenes  `#autonomous-vehicles` `#camera` `#canyons` `#dataset` `#lidar` `#localization` `#mapping` `#slam` `#urban`
- **[ydsf16/imu_gps_localization](https://github.com/ydsf16/imu_gps_localization)** · `C++` — Using error-state Kalman filter to fuse the IMU and GPS data for localization.
- **[zju3dv/vig-init](https://github.com/zju3dv/vig-init)** · `C++` — Rapid and Robust Monocular Visual-Inertial Initialization with Gravity Estimation via Vertical Edges  `#slam` `#vio` `#vislam`
- **[zm0612/eskf-gps-imu-fusion](https://github.com/zm0612/eskf-gps-imu-fusion)** · `C++` — 误差状态卡尔曼ESKF滤波器融合GPS和IMU，实现更高精度的定位

## 📦 建图 / 3D 重建 / 体素 / 场图
*(8 项)*

- **[ANYbotics/grid_map](https://github.com/ANYbotics/grid_map)** · `C++` — Universal grid map library for mobile robotic mapping  `#costmap` `#cpp` `#elevation` `#grid-map` `#height-map` `#mapping` `#navigation` `#occupancy` `#octopmap` `#opencv` `#pcl` `#ros` `#rviz` `#terrain`
- **[ethz-asl/voxblox](https://github.com/ethz-asl/voxblox)** · `C++` — A library for flexible voxel-based mapping, mainly focusing on truncated and Euclidean signed distance fields.  `#mapping` `#robotics` `#voxblox`
- **[hovsg/HOV-SG](https://github.com/hovsg/HOV-SG)** · `Python` — [RSS2024] Official implementation of "Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation"  `#3d-scene-graph` `#natural-language-understanding` `#open-vocabulary` `#robot-navigation` `#robot-planning`
- **[niessner/VoxelHashing](https://github.com/niessner/VoxelHashing)** · `C++` — [Siggraph Asia 2013] Large-Scale, Real-Time 3D Reconstruction  `#3d-reconstruction` `#computer-vision` `#kinect`
- **[NVIDIA-ISAAC-ROS/isaac_ros_nvblox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox)** · `C++` — NVIDIA-accelerated 3D scene reconstruction and Nav2 local costmap provider using nvblox  `#3d-reconstruction` `#gpu` `#jetson` `#nvidia` `#robotics` `#ros` `#ros2-humble`
- **[nvidia-isaac/nvblox](https://github.com/nvidia-isaac/nvblox)** · `C++` — A GPU-accelerated TSDF and ESDF library for robots equipped with RGB-D cameras.
- **[OctoMap/octomap](https://github.com/OctoMap/octomap)** · `C++` — An Efficient Probabilistic 3D Mapping Framework Based on Octrees. Contains the main OctoMap library, the viewer octovis, and dynamicEDT3D.
- **[zhujun3753/i-octree](https://github.com/zhujun3753/i-octree)** · `C++` — [ICRA2024] Implementation of A Fast, Lightweight, and Dynamic Octree for Proximity Search

## 🚗 自动驾驶
*(6 项)*

- **[ApolloAuto/apollo](https://github.com/ApolloAuto/apollo)** · `C++` — An open autonomous driving platform  `#apollo` `#autonomous-driving` `#autonomous-vehicles` `#autonomy` `#self-driving-car`
- **[Arlo0o/StereoScene](https://github.com/Arlo0o/StereoScene)** · `Python` — [IJCAI 2024]Official PyTorch Implementation of Bridging Stereo Geometry and BEV Representation with Reliable Mutual Interaction for Semantic Scene Completion  `#3d-scene-understanding` `#artificial-intelligence` `#autonomous-driving` `#autonomous-vehicles` `#computer-vision` `#deep-learning` `#machine-learning` `#pytorch` `#semantic-kitti` `#semantic-scene-completion` `#semantic-scene-understanding`
- **[carla-simulator/carla](https://github.com/carla-simulator/carla)** · `C++` — Open-source simulator for autonomous driving research.  `#ai` `#artificial-intelligence` `#autonomous-driving` `#autonomous-vehicles` `#carla` `#carla-simulator` `#computer-vision` `#cross-platform` `#deep-learning` `#deep-reinforcement-learning` `#imitation-learning` `#research` `#ros` `#self-driving-car` `#simulator` `#ue4` `#unreal-engine-4`
- **[JOP-Lee/READ](https://github.com/JOP-Lee/READ)** · `Python` — AAAI2023，implementation of "READ:  Large-Scale Neural Scene Rendering for Autonomous Driving", the experimental results are significantly better than Nerf-based methods  `#driving` `#kitti` `#nerf` `#neural-rendering` `#view-synthesis`
- **[MCZhi/Driving-IRL-NGSIM](https://github.com/MCZhi/Driving-IRL-NGSIM)** · `Python` — [T-ITS] Driving Behavior Modeling using Naturalistic Human Driving Data with Inverse Reinforcement Learning  `#autonomous-driving` `#inverse-reinforcement-learning`
- **[NVlabs/X-MOBILITY](https://github.com/NVlabs/X-MOBILITY)** · `Python` — X-MOBILITY

## 👀 感知 / 计算机视觉 (检测/跟踪/姿态/光流)
*(22 项)*

- **[aCodeDog/OmniPerception](https://github.com/aCodeDog/OmniPerception)** · `Python` — (无描述)
- **[Ahmednull/L2CS-Net](https://github.com/Ahmednull/L2CS-Net)** · `Python` — The official PyTorch implementation of L2CS-Net for gaze estimation and tracking  `#3d` `#analysis` `#appearance` `#deep-learning` `#eye-tracking` `#eyetracking` `#gaze` `#gaze-estimation` `#gaze-estimation-model` `#gaze-tracking` `#gaze360` `#mpiigaze` `#pytorch` `#pytorch-implementation` `#unconstrained`
- **[AIDajiangtang/Superpoint-LightGlue-Image-Stiching](https://github.com/AIDajiangtang/Superpoint-LightGlue-Image-Stiching)** · `C++` — OpenCV图像拼接Pipeline集成 SuperPoint 、LightGlue 特征点检测和匹配深度学习模型  `#deeplearning` `#feature-extraction` `#feature-matching` `#lightglue` `#opencv` `#superpoint`
- **[aipiano/guided-filter-point-cloud-denoise](https://github.com/aipiano/guided-filter-point-cloud-denoise)** · `Python` — Use guided filter to reduce the noise of a 3d point cloud.
- **[AnjieCheng/SpatialRGPT](https://github.com/AnjieCheng/SpatialRGPT)** · `Python` — [NeurIPS'24] This repository is the implementation of "SpatialRGPT: Grounded Spatial Reasoning in Vision Language Models"  `#spatial-reasoning` `#vision-language-model`
- **[apple/ml-fastvlm](https://github.com/apple/ml-fastvlm)** · `Python` — This repository contains the official implementation of "FastVLM: Efficient Vision Encoding for Vision Language Models" - CVPR 2025
- **[apple/ml-hugs](https://github.com/apple/ml-hugs)** · `Python` — Official repository of HUGS: Human Gaussian Splats (CVPR 2024)  `#gaussian-splatting` `#neural-rendering`
- **[CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)** · `C++` — OpenPose: Real-time multi-person keypoint detection library for body, face, hands, and foot estimation  `#caffe` `#computer-vision` `#cpp` `#cvpr-2017` `#deep-learning` `#face` `#foot-estimation` `#hand-estimation` `#human-behavior-understanding` `#human-pose` `#human-pose-estimation` `#keypoint-detection` `#keypoints` `#machine-learning` `#multi-person` `#opencv` `#openpose` `#pose` `#pose-estimation` `#real-time`
- **[cvg/LightGlue](https://github.com/cvg/LightGlue)** · `Python` — LightGlue: Local Feature Matching at Light Speed (ICCV 2023)  `#deep-learning` `#image-matching` `#pose-estimation` `#transformers`
- **[deepinsight/insightface](https://github.com/deepinsight/insightface)** · `Python` — State-of-the-art 2D and 3D Face Analysis Project  `#age-estimation` `#arcface` `#face-alignment` `#face-detection` `#face-recognition` `#mxnet` `#oneflow` `#paddlepaddle` `#pytorch` `#retinaface`
- **[drinkingcoder/FlowFormer-Official](https://github.com/drinkingcoder/FlowFormer-Official)** · `Python` — (无描述)
- **[LMD0311/PointMamba](https://github.com/LMD0311/PointMamba)** · `Python` — [NeurIPS 2024] PointMamba: A Simple State Space Model for Point Cloud Analysis  `#3d-point-clouds` `#computer-vision` `#mamba` `#state-space-model`
- **[MCG-NJU/MixFormer](https://github.com/MCG-NJU/MixFormer)** · `Python` — [CVPR 2022 Oral & TPAMI 2024] MixFormer: End-to-End Tracking with Iterative Mixed Attention  `#cvpr2022` `#tracking` `#vot`
- **[MCG-NKU/AMT](https://github.com/MCG-NKU/AMT)** · `Python` — Official code for "AMT: All-Pairs Multi-Field Transforms for Efficient Frame Interpolation" (CVPR2023)  `#backward-warp` `#cvpr2023` `#frame-interpolation` `#optical-flow` `#slomo` `#video` `#video-generation`
- **[mikel-brostrom/boxmot](https://github.com/mikel-brostrom/boxmot)** · `Python` — BoxMOT: Pluggable python and c++ SOTA multi-object tracking modules with support for axis-aligned and oriented bounding boxes  `#boosttrack` `#botsort` `#bytetrack` `#deep-learning` `#deepocsort` `#machine-learning` `#mot` `#mots` `#multi-object-tracking` `#multi-object-tracking-segmentation` `#ocsort` `#oriented-bounding-box-tracking` `#segmentation` `#strongsort` `#tensorrt` `#tracking-by-detection` `#yolo`
- **[NirAharon/BoT-SORT](https://github.com/NirAharon/BoT-SORT)** · `Jupyter Notebook` — BoT-SORT: Robust Associations Multi-Pedestrian Tracking  `#multi-object-tracker` `#multi-object-tracking` `#multi-pedestrian-tracking` `#pytorch` `#tracking-by-detection` `#yolov7` `#yolox`
- **[princeton-vl/RAFT-Stereo](https://github.com/princeton-vl/RAFT-Stereo)** · `Python` — (无描述)
- **[switchablenorms/DeepFashion2](https://github.com/switchablenorms/DeepFashion2)** · `Jupyter Notebook` — DeepFashion2 Dataset https://arxiv.org/pdf/1901.07973.pdf
- **[THU-MIG/yolov10](https://github.com/THU-MIG/yolov10)** · `Python` — YOLOv10: Real-Time End-to-End Object Detection [NeurIPS 2024]
- **[XiaoyuShi97/FlowFormerPlusPlus](https://github.com/XiaoyuShi97/FlowFormerPlusPlus)** · `Python` — FlowFormer++: Masked Cost Volume Autoencoding for Pretraining Optical Flow Estimation
- **[yformer/EfficientSAM](https://github.com/yformer/EfficientSAM)** · `Jupyter Notebook` — EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything
- **[zylinzy/GazeHTA](https://github.com/zylinzy/GazeHTA)** · `Python` — (无描述)

## 🎮 仿真平台 / Simulators
*(8 项)*

- **[cyberbotics/webots](https://github.com/cyberbotics/webots)** · `C++` — Webots Robot Simulator  `#3d-engine` `#ai` `#autonomous-vehicles` `#computer-vision` `#fluid-dynamics` `#multi-platform` `#open-source` `#physics-engine` `#robot` `#robot-simulation` `#robot-simulator` `#robotics` `#robotics-simulation` `#robots` `#ros` `#ros2` `#simulated-robots` `#simulation` `#simulator` `#webots`
- **[Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world)** · `Python` — Simulation platform for general-purpose robotics & embodied AI learning.
- **[isaac-sim/IsaacLab-Arena](https://github.com/isaac-sim/IsaacLab-Arena)** · `Python` — Isaac Lab - Arena is a robotics simulation framework that enhances NVIDIA Isaac Lab by providing a composable, scalable system for creating diverse simulation environments and evaluating robot learning policies. The framework enables developers to rapidly prototype and test robotic tasks with various robot embodiments, objects, and environments.
- **[isaac-sim/IsaacSim](https://github.com/isaac-sim/IsaacSim)** · `Python` — NVIDIA Isaac Sim™ is an open-source application on NVIDIA Omniverse for developing, simulating, and testing AI-driven robots in realistic virtual environments.
- **[mani-skill/ManiSkill](https://github.com/mani-skill/ManiSkill)** · `Python` — SAPIEN Manipulation Skill Framework, an open source GPU parallelized robotics simulator and benchmark  `#embodied-ai` `#reinforcement-learning` `#robot-learning` `#robot-manipulation` `#robotics` `#simulation`
- **[mujocolab/mjlab](https://github.com/mujocolab/mjlab)** · `Python` — Isaac Lab API, powered by MuJoCo-Warp, for RL and robotics research  `#isaaclab` `#mujoco` `#mujoco-warp` `#reinforcement-learning` `#robotics-simulation`
- **[NVlabs/ProtoMotions](https://github.com/NVlabs/ProtoMotions)** · `Python` — ProtoMotions is a GPU-accelerated simulation and learning framework for training physically simulated digital humans and humanoid robots.  `#character-animation` `#digital-human` `#humanoid` `#humanoid-robots` `#physics-simulation` `#reinforcement-learning`
- **[pal-robotics/tiago_simulation](https://github.com/pal-robotics/tiago_simulation)** · `Python` — (无描述)  `#advanced-navigation` `#humble` `#manipulator` `#mobile` `#mobile-base` `#mobile-manipulator` `#navigation` `#noetic` `#ros` `#ros2` `#ros2-humble` `#simulation`

## 🌐 World Model & 序列模型 (SSM)
*(7 项)*

- **[dreamzero0/dreamzero](https://github.com/dreamzero0/dreamzero)** · `Python` — Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals
- **[leggedrobotics/robotic_world_model](https://github.com/leggedrobotics/robotic_world_model)** · `Python` — Repository for our papers: Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics and Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots
- **[nvidia-cosmos/cosmos-predict2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5)** · `Python` — Cosmos-Predict2.5, the latest version of the Cosmos World Foundation Models (WFMs) family, specialized for simulating and predicting the future state of the world in the form of video.  `#foundational-models` `#video-generation` `#world-models`
- **[NVIDIA/cosmos](https://github.com/NVIDIA/cosmos)** · `Jupyter Notebook` — NVIDIA Cosmos is an open platform of world models, datasets, and tools that enables developers to build Physical AI for robots, autonomous vehicles, smart infrastructure, and more.
- **[state-spaces/mamba](https://github.com/state-spaces/mamba)** · `Python` — Mamba SSM architecture
- **[state-spaces/s4](https://github.com/state-spaces/s4)** · `Jupyter Notebook` — Structured state space sequence models  `#pytorch` `#sequence-models` `#state-space-models`
- **[thu-ml/Motus](https://github.com/thu-ml/Motus)** · `Python` — Official code of Motus: A Unified Latent Action World Model  `#diffusion-model` `#robotic-manipulation` `#robotics` `#unidiffuser` `#video-generation` `#vision-language-action-model` `#world-model`

## 🧰 机器人工具 / 库 / SDK
*(13 项)*

- **[anassinator/ilqr](https://github.com/anassinator/ilqr)** · `Python` — Iterative Linear Quadratic Regulator with auto-differentiatiable dynamics models  `#auto-differentiation` `#cartpole` `#control-systems` `#ddp` `#differential-dynamic-programming` `#dynamics-models` `#ilqg` `#ilqr` `#model-predictive-control` `#model-predictive-controller` `#mpc` `#mpc-control` `#non-linear-optimization` `#optimal-control` `#pendulum` `#theano` `#trajectory-optimization` `#trajectory-tracking`
- **[CVHub520/X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling)** · `Python` — Effortless data labeling with AI support from Segment Anything and other awesome models.  `#artificial-intelligence` `#clip` `#computer-vision` `#deep-learning` `#groundingdino` `#image-annotation-tool` `#image-classification` `#image-labeling-tool` `#image-matting` `#instance-segmentation` `#machine-learning` `#object-detection` `#ocr` `#onnxruntime` `#paddlepaddle` `#pose-estimation` `#rotated-object-detection` `#sam` `#vision-language-model` `#yolo`
- **[fzi-forschungszentrum-informatik/cartesian_controllers](https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers)** · `C++` — A set of Cartesian controllers for the ROS1 and ROS2-control framework.
- **[geographiclib/geographiclib](https://github.com/geographiclib/geographiclib)** · `C++` — Main repository for GeographicLib
- **[google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)** · `C++` — Real-time behaviour synthesis with MuJoCo, using Predictive Control  `#model-predictive-control` `#motor-control` `#mpc` `#mpc-control` `#mujoco` `#predictive-control`
- **[HansZ8/RoboJuDo](https://github.com/HansZ8/RoboJuDo)** · `Python` — A plug-and-play deploy framework for robots. Just deploy, just do.  `#amo` `#asap` `#beyondmimic` `#deploy` `#g1` `#h1` `#human2humanoid` `#humanoid` `#kungfubot` `#kungfubot2` `#pbhc` `#robot` `#twist` `#unitree`
- **[MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)** · `Python` — Python package for the evaluation of odometry and SLAM  `#benchmark` `#euroc` `#evaluation` `#kitti` `#mapping` `#metrics` `#odometry` `#robotics` `#ros` `#ros2` `#slam` `#trajectory` `#trajectory-analysis` `#trajectory-evaluation` `#tum`
- **[NVlabs/curobo](https://github.com/NVlabs/curobo)** · `Python` — CUDA Accelerated Robot Library  `#cuda` `#motion-planning` `#pytorch` `#robotics`
- **[onnx/onnx](https://github.com/onnx/onnx)** · `Python` — Open standard for machine learning interoperability  `#ai` `#artificial-intelligence` `#deep-learning` `#deep-neural-networks` `#dnn` `#keras` `#machine-learning` `#ml` `#neural-network` `#onnx` `#pytorch` `#scikit-learn` `#tensorflow`
- **[OpenLegged/URDF-Studio](https://github.com/OpenLegged/URDF-Studio)** · `TypeScript` — URDF-Studio is a web-based visual URDF robot modeler with 3D workspace, structured skeleton/detail/hardware workflows, motor library integration, MuJoCo export, and AI assistance.  `#robot` `#robotics` `#urdf` `#urdf-design`
- **[petercorke/robotics-toolbox-python](https://github.com/petercorke/robotics-toolbox-python)** · `C++` — Robotics Toolbox for Python  `#dynamics` `#hessian` `#jacobian` `#kinematics` `#motion-planning` `#python` `#robot-manipulator` `#robotics` `#robotics-control` `#robotics-simulation` `#robotics-toolbox` `#trajectory-generation`
- **[vietanhdev/anylabeling](https://github.com/vietanhdev/anylabeling)** · `Python` — Effortless AI-assisted data labeling with AI support from YOLO, Segment Anything (SAM+SAM2/2.1+SAM3), MobileSAM!!  `#auto-labeling` `#computer-vision` `#labeling` `#labeling-tool` `#mobilesam` `#onnx` `#sam2` `#segment-anything` `#segment-anything-2` `#yolo` `#yolov8`
- **[wandb/wandb](https://github.com/wandb/wandb)** · `Python` — The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production.  `#ai` `#collaboration` `#data-science` `#data-versioning` `#deep-learning` `#experiment-track` `#hyperparameter-optimization` `#hyperparameter-search` `#hyperparameter-tuning` `#jax` `#keras` `#machine-learning` `#ml-platform` `#mlops` `#model-versioning` `#pytorch` `#reinforcement-learning` `#reproducibility` `#tensorflow`

## 🤖 ROS / 驱动 / 集成包
*(4 项)*

- **[anujjain-dev/unitree-go2-ros2](https://github.com/anujjain-dev/unitree-go2-ros2)** · `C++` — Developing robot description model for Unitree Go2 robot configured with Champ Legged Robots Research Repository  `#champ` `#gazebo` `#go2` `#ros2` `#unitree` `#unitree-go2`
- **[realsenseai/meta-intel-realsense](https://github.com/realsenseai/meta-intel-realsense)** · `BitBake` — Yocto layer for realsense-sdk and librealsense
- **[ros-drivers/usb_cam](https://github.com/ros-drivers/usb_cam)** · `C++` — A ROS Driver for V4L2 USB Cameras
- **[ros/meta-ros](https://github.com/ros/meta-ros)** · `BitBake` — OpenEmbedded Layers for ROS 1 and ROS 2

## 🧠 LLM / Agent / AI Coding 工具
*(10 项)*

- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · `TypeScript` — GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a git repository (Github, Gitlab, Azure, Local) or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · `Python` — 🌐 Make websites accessible for AI agents. Automate tasks online with ease.  `#ai-agents` `#ai-tools` `#browser-automation` `#browser-use` `#llm` `#playwright` `#python`
- **[cmjang/mjlab-skillkit](https://github.com/cmjang/mjlab-skillkit)** · `Shell` — AI coding skill kit for IsaacLab migration and mjlab-native development  `#agent-tools` `#ai-coding` `#claude-code` `#codex` `#cursor` `#developer-tools` `#gemini-cli` `#isaaclab` `#migration` `#migration-tooling` `#mjlab` `#mujoco` `#reinforcement-learning` `#robotics` `#simulation` `#skill-library` `#task-authoring`
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · `Rust` — A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent. Only official website: ccswitch.io  `#ai-tools` `#claude-code` `#codex` `#desktop-app` `#hermes` `#hermes-agent` `#mcp` `#minimax` `#omo` `#open-source` `#openclaw` `#openclaw-ui` `#opencode` `#provider-management` `#rust` `#skills` `#skills-management` `#tauri` `#typescript` `#wsl-support`
- **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** · `TypeScript` — Spec-driven development (SDD) for AI coding assistants.  `#ai` `#context-engineering` `#engineering` `#planning` `#prd` `#sdd` `#sdlc` `#spec` `#spec-driven-development` `#specification`
- **[HKUDS/DeepCode](https://github.com/HKUDS/DeepCode)** · `Python` — "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)"  `#agentic-coding` `#llm-agent`
- **[HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness)** · `Python` — "OpenHarness: Open Agent Harness with a Built-in Personal Agent--Ohmo!"
- **[larksuite/cli](https://github.com/larksuite/cli)** · `Go` — The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.
- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · `TypeScript` — Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞  `#ai` `#assistant` `#crustacean` `#molty` `#openclaw` `#own-your-data` `#personal`
- **[toon-format/toon](https://github.com/toon-format/toon)** · `TypeScript` — 🎒 Token-Oriented Object Notation (TOON) – Compact, human-readable, schema-aware JSON for LLM prompts. Spec, benchmarks, TypeScript SDK.  `#data-format` `#llm` `#serialization` `#tokenization`

## 📊 时间序列 / 金融预测
*(3 项)*

- **[moyuweiqing/A-stock-prediction-algorithm-based-on-machine-learning](https://github.com/moyuweiqing/A-stock-prediction-algorithm-based-on-machine-learning)** · `HTML` — （陆续更新）重新整理过的基于机器学习的股票价格预测算法，里面包含了基本的回测系统以及各种不同的机器学习算法的股票价格预测，包含：LSTM算法、Prophet算法、AutoARIMA、朴素贝叶斯、SVM、随机森林等  `#gaussiannb` `#prophet` `#python` `#sklearn` `#svm` `#tushare`
- **[yangwohenmai/LSTM](https://github.com/yangwohenmai/LSTM)** · `Python` — 基于LSTM的时间序列预测研究  `#forecast` `#lstm`
- **[yangwohenmai/TimeSeriesForecasting](https://github.com/yangwohenmai/TimeSeriesForecasting)** · `Python` — 基于统计学的时间序列预测(AR,ARM).

## 📚 学习资源 / 教程 / Awesome List
*(30 项)*

- **[aCodeDog/awesome-loco-manipulation](https://github.com/aCodeDog/awesome-loco-manipulation)** · `CMake` — (无描述)
- **[agilexrobotics/Agilex-College](https://github.com/agilexrobotics/Agilex-College)** · `C++` — Agilex College
- **[ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code)** · `—` — 500 AI Machine learning Deep learning Computer vision NLP Projects with code  `#artificial-intelligence` `#artificial-intelligence-projects` `#awesome` `#computer-vision` `#computer-vision-project` `#data-science` `#deep-learning` `#deep-learning-project` `#machine-learning` `#machine-learning-projects` `#nlp` `#nlp-projects` `#python`
- **[balloonwj/CppGuide](https://github.com/balloonwj/CppGuide)** · `—` — C/C++学习，后端开发进阶指南。
- **[CHH3213/chhRobotics_CPP](https://github.com/CHH3213/chhRobotics_CPP)** · `C++` — 自动驾驶规划控制常用算法c++代码实现
- **[datawhalechina/easy-rl](https://github.com/datawhalechina/easy-rl)** · `Jupyter Notebook` — 强化学习中文教程（蘑菇书🍄），在线阅读地址：https://datawhalechina.github.io/easy-rl/  `#a3c` `#ddpg` `#deep-reinforcement-learning` `#double-dqn` `#dqn` `#dueling-dqn` `#easy-rl` `#imitation-learning` `#policy-gradient` `#ppo` `#q-learning` `#reinforcement-learning` `#sarsa` `#td3`
- **[datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm)** · `Jupyter Notebook` — 📚 从零开始构建大模型  `#agent` `#llm` `#rag`
- **[Ewenwan/MVision](https://github.com/Ewenwan/MVision)** · `C++` — 机器人视觉 移动机器人 VS-SLAM ORB-SLAM2 深度学习目标检测 yolov3 行为检测 opencv  PCL 机器学习 无人驾驶  `#cnn` `#deep-learning` `#machine-vision` `#opencv` `#pcl` `#robot` `#slam`
- **[Ewenwan/UCL-DeepReinforcementLearning](https://github.com/Ewenwan/UCL-DeepReinforcementLearning)** · `—` — 一门由AlphaGo项目负责人David Sliver，在UCL(伦敦大学)主讲的强化学习经典课程
- **[gaiyi7788/awesome-legged-locomotion-learning](https://github.com/gaiyi7788/awesome-legged-locomotion-learning)** · `—` — A curated list of resources relevant to legged locomotion learning of robotics.  `#awesome` `#locomotion` `#reinforcement-learning` `#robotics`
- **[google-research/tuning_playbook](https://github.com/google-research/tuning_playbook)** · `—` — A playbook for systematically maximizing the performance of deep learning models.
- **[IRVING-L/Algorithm_fromBilibili](https://github.com/IRVING-L/Algorithm_fromBilibili)** · `—` — 《B站-青岛大学-王卓老师-数据结构与算法基础》自学心得、笔记（C++语言实现）  `#algorithm` `#cpp11`
- **[jonyzhang2023/awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)** · `—` — A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches.
- **[kaieye/2022-Machine-Learning-Specialization](https://github.com/kaieye/2022-Machine-Learning-Specialization)** · `Jupyter Notebook` — (无描述)
- **[Kedreamix/Awesome-Talking-Head-Synthesis](https://github.com/Kedreamix/Awesome-Talking-Head-Synthesis)** · `—` — 💬 An extensive collection of exceptional resources dedicated to the captivating world of talking face synthesis!   ⭐ If you find this repo useful, please give it a star! 🤩  `#arxiv` `#audio-driven` `#paper` `#synthesis` `#talking-face-generation` `#talking-head` `#talking-head-video-generation`
- **[Light-City/CPlusPlusThings](https://github.com/Light-City/CPlusPlusThings)** · `C++` — C++那些事  `#cplusplus` `#cpp` `#cpp11` `#cpp14`
- **[LiZhengXiao99/Navigation-Learning](https://github.com/LiZhengXiao99/Navigation-Learning)** · `—` — 我的导航算法学习笔记，内容涵盖导航定位开源程序的源码解读、开源项目梳理、书籍讲义、博客翻译、教程讲座推荐；所有内容都可以随意转载，原始文件都放在这里了，大家可以在我的基础上整理出自己的一些文档。（Tips：①主要是写给初学者，已经有基础的同学应该多看论文和代码，看我的笔记学不到啥；②仓库持续更新中，不建议 fork）  `#gnss` `#gnss-sdr` `#gps` `#ins` `#kf-gins` `#location` `#navigation` `#ob-gins` `#orb` `#ppp` `#ppplib` `#rtk` `#rtklib` `#slam` `#softgnss` `#tgins` `#vins` `#vio`
- **[Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms)** · `Jupyter Notebook` — 《动手学大模型Dive into LLMs》系列编程实践教程
- **[Ly0n/awesome-robotic-tooling](https://github.com/Ly0n/awesome-robotic-tooling)** · `—` — Tooling for professional robotic development in C++ and Python with a touch of ROS, autonomous driving and aerospace.  `#aerospace` `#artificial-intelligence` `#automotive` `#autonomous-driving` `#awesome` `#awesome-list` `#cplusplus` `#cpp` `#lidar` `#machine-learning` `#mapping` `#point-cloud` `#python` `#robot` `#robotic` `#robotics` `#ros` `#ros2` `#self-driving-car` `#slam`
- **[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · `—` — Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks.  `#course` `#large-language-models` `#llm` `#machine-learning` `#roadmap`
- **[MrNeRF/awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting)** · `HTML` — Curated list of papers and resources focused on 3D Gaussian Splatting, intended to keep pace with the anticipated surge of research in the coming months.  `#3d-gaussian-splatting` `#3dgs` `#gaussian-splatting` `#nerf` `#neural-rendering`
- **[nebula-beta/SLAM-Jobs](https://github.com/nebula-beta/SLAM-Jobs)** · `—` — 这个一份SLAM/SFM求职指南，旨在帮助视觉SLAM/SFM的小伙伴们能够找到更好的工作。
- **[NTUMARS/Awesome-World-Model-for-Robotics-Policy](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy)** · `—` — (无描述)
- **[RussTedrake/underactuated](https://github.com/RussTedrake/underactuated)** · `HTML` — The course text for MIT 6.832 (and 6.832x on edX)
- **[ShangtongZhang/reinforcement-learning-an-introduction](https://github.com/ShangtongZhang/reinforcement-learning-an-introduction)** · `Python` — Python Implementation of Reinforcement Learning: An Introduction  `#artificial-intelligence` `#reinforcement-learning`
- **[simoninithomas/Deep_reinforcement_learning_Course](https://github.com/simoninithomas/Deep_reinforcement_learning_Course)** · `Jupyter Notebook` — Implementations from the free course Deep Reinforcement Learning with Tensorflow and PyTorch  `#a2c` `#actor-critic` `#deep-learning` `#deep-q-learning` `#deep-q-network` `#deep-reinforcement-learning` `#ppo` `#pytorch` `#qlearning` `#tensorflow` `#tensorflow-tutorials` `#unity`
- **[TianxingChen/Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide)** · `—` — [Lumina具身智能社区] 具身智能技术指南 Embodied-AI-Guide  `#embodied` `#embodied-ai` `#guide` `#robot` `#robotic` `#robotics` `#tutorial`
- **[ts-flake/d2lrobot](https://github.com/ts-flake/d2lrobot)** · `Jupyter Notebook` — A collection of tutorials, notes, and practices for learning robotics.
- **[udacity/deep-reinforcement-learning](https://github.com/udacity/deep-reinforcement-learning)** · `Jupyter Notebook` — Repo for the Deep Reinforcement Learning Nanodegree program  `#cross-entropy` `#ddpg` `#deep-reinforcement-learning` `#dqn` `#dynamic-programming` `#hill-climbing` `#ml-agents` `#neural-networks` `#openai-gym` `#openai-gym-solutions` `#ppo` `#pytorch` `#pytorch-rl` `#reinforcement-learning` `#reinforcement-learning-algorithms` `#rl-algorithms`
- **[zhouyong1234/SLAM-All-In-One](https://github.com/zhouyong1234/SLAM-All-In-One)** · `C++` — SLAM汇总，包括多传感器融合建图、定位、VIO系列、常用工具包、开源代码注释和公式推导、文章综述

## ❓ 其他 / 待分类
*(2 项)*

- **[amazon-far/holosoma](https://github.com/amazon-far/holosoma)** · `Python` — (无描述)
- **[guanboang/PoloMan](https://github.com/guanboang/PoloMan)** · `MATLAB` — (无描述)
