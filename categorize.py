#!/usr/bin/env python3
"""把 stars_meta.jsonl 按预设类别归类，输出 stars_grouped.md。"""
import json
import unicodedata
from collections import defaultdict
from pathlib import Path

META = Path("/home/zichen/Downloads/stars_meta.jsonl")
OUT = Path("/home/zichen/Downloads/stars_grouped.md")

# 类目顺序与中英文名
CATEGORIES = [
    ("vla",        "🤖 VLA & 具身智能基础模型 (Vision-Language-Action / Foundation Models)"),
    ("manip",      "🦾 模仿学习 & 机械臂操作 / Teleoperation"),
    ("soarm",      "🦾 SO-ARM / SO-101 等低成本机械臂平台"),
    ("humanoid",   "🧍 人形机器人 (Humanoid)"),
    ("quadruped",  "🐕 四足机器人 (Quadruped)"),
    ("loco",       "🚶 Locomotion / 腿式运动学习"),
    ("rl",         "🎯 强化学习 (RL 算法 / Sim-to-Real / 课程)"),
    ("nav",        "🧭 移动机器人导航"),
    ("uav",        "🛩️ 无人机 / UAV / Aerial Robotics"),
    ("slam",       "🗺️ SLAM (Visual / LiDAR / RGBD)"),
    ("vio_gnss",   "📡 VIO / GNSS / 多传感器融合 / 标定"),
    ("mapping",    "📦 建图 / 3D 重建 / 体素 / 场图"),
    ("driving",    "🚗 自动驾驶"),
    ("perception", "👀 感知 / 计算机视觉 (检测/跟踪/姿态/光流)"),
    ("sim",        "🎮 仿真平台 / Simulators"),
    ("worldmodel", "🌐 World Model & 序列模型 (SSM)"),
    ("tools",      "🧰 机器人工具 / 库 / SDK"),
    ("ros",        "🤖 ROS / 驱动 / 集成包"),
    ("aicode",     "🧠 LLM / Agent / AI Coding 工具"),
    ("timeseries", "📊 时间序列 / 金融预测"),
    ("resource",   "📚 学习资源 / 教程 / Awesome List"),
    ("other",      "❓ 其他 / 待分类"),
]

# 242 个 repo → 类别映射
M = {
    # 1-10
    "amap-cvlab/ABot-Navigation": "nav",
    "wsakobe/TrackVLA": "vla",
    "QwenLM/Qwen-RobotNav": "vla",
    "RLinf/LaWAM": "vla",
    "legalaspro/so101-ros-physical-ai": "soarm",
    "tonyzhaozh/aloha": "manip",
    "tonyzhaozh/act": "manip",
    "cmjang/mjlab-skillkit": "aicode",
    "isaac-sim/IsaacSim": "sim",
    "fzi-forschungszentrum-informatik/cartesian_controllers": "tools",
    # 11-20
    "commanderfun/STS3215": "soarm",
    "NVIDIA/cosmos": "worldmodel",
    "farion1231/cc-switch": "aicode",
    "ts-flake/d2lrobot": "resource",
    "HKUDS/OpenHarness": "aicode",
    "abhigyanpatwari/GitNexus": "aicode",
    "nvidia-cosmos/cosmos-predict2.5": "worldmodel",
    "mani-skill/ManiSkill": "sim",
    "dexmal/dexbotic": "vla",
    "MuammerBay/isaac_so_arm101": "soarm",
    # 21-30
    "thu-ml/Motus": "worldmodel",
    "NVlabs/cosmos-policy": "vla",
    "Robbyant/lingbot-va": "vla",
    "mujocolab/mjlab": "sim",
    "larksuite/cli": "aicode",
    "allenai/molmoact2": "vla",
    "NTUMARS/Awesome-World-Model-for-Robotics-Policy": "resource",
    "husky/husky_manipulation": "manip",
    "FluxVLA/FluxVLA": "vla",
    "upasana099/Autonomous-Navigation-of-Mobile-Manipulator": "nav",
    # 31-40
    "priyasundaresan/homer": "vla",
    "petercorke/robotics-toolbox-python": "tools",
    "zhanghengsjtu/mobile_manipulator_ros_simulation": "manip",
    "TheRobotStudio/SO-ARM100": "soarm",
    "MarkFzp/act-plus-plus": "manip",
    "MarkFzp/mobile-aloha": "manip",
    "anubhav1772/6-dof-robotic-arm": "manip",
    "lFatality/ros_moveit_gazebo_ws": "manip",
    "dreamzero0/dreamzero": "worldmodel",
    "NVlabs/GR00T-WholeBodyControl": "humanoid",
    # 41-50
    "leggedrobotics/robotic_world_model": "worldmodel",
    "abmoRobotics/RLRoverLab": "rl",
    "openclaw/openclaw": "aicode",
    "LeCAR-Lab/BFM-Zero": "humanoid",
    "danijar/dreamerv3": "rl",
    "leggedrobotics/rsl_rl": "rl",
    "Roboparty/roboto_origin": "humanoid",
    "project-instinct/InstinctLab": "rl",
    "OpenLegged/URDF-Studio": "tools",
    "Zhefan-Xu/NavRL": "nav",
    # 51-60
    "pal-robotics/tiago_simulation": "sim",
    "openvla/openvla": "vla",
    "jonyzhang2023/awesome-embodied-vla-va-vln": "resource",
    "browser-use/browser-use": "aicode",
    "huggingface/lerobot": "manip",
    "NVlabs/X-MOBILITY": "driving",
    "isaac-sim/IsaacLab-Arena": "sim",
    "NVlabs/COMPASS": "rl",
    "NVIDIA/Isaac-GR00T": "vla",
    "WM-PO/WMPO": "vla",
    # 61-70
    "aCodeDog/legged-robots-manipulation": "manip",
    "Physical-Intelligence/openpi": "vla",
    "RoboTwin-Platform/RoboTwin": "manip",
    "Genesis-Embodied-AI/genesis-world": "sim",
    "aCodeDog/awesome-loco-manipulation": "resource",
    "agilexrobotics/Agilex-College": "resource",
    "yang-zj1026/legged-loco": "loco",
    "TianxingChen/Embodied-AI-Guide": "resource",
    "lucidrains/locoformer": "loco",
    "Robotics-STAR-Lab/REMANI-Planner": "manip",
    # 71-80
    "NVlabs/curobo": "tools",
    "InternRobotics/HoST": "humanoid",
    "Open-X-Humanoid/TienKung-Lab": "humanoid",
    "anujjain-dev/unitree-go2-ros2": "ros",
    "wandb/wandb": "tools",
    "amazon-far/holosoma": "other",
    "81578823/3D_navigation_PCTplanner": "nav",
    "HKUDS/DeepCode": "aicode",
    "aCodeDog/OmniPerception": "perception",
    "chengxuxin/extreme-parkour": "loco",
    # 81-90
    "ZJU-FAST-Lab/ego-planner-swarm": "uav",
    "HUST-3W/GMR_autoik": "humanoid",
    "2473o/PCT_planner": "nav",
    "zst1406217/VR-Robo": "vla",
    "byangw/PCT_planner": "nav",
    "NVIDIA-ISAAC-ROS/isaac_ros_nvblox": "mapping",
    "state-spaces/mamba": "worldmodel",
    "state-spaces/s4": "worldmodel",
    "LMD0311/PointMamba": "perception",
    "HybridRobotics/whole_body_tracking": "rl",
    # 91-100
    "NVlabs/ProtoMotions": "sim",
    "HansZ8/RoboJuDo": "tools",
    "DAVIAN-Robotics/PHUMA": "humanoid",
    "zju3dv/GVHMR": "humanoid",
    "Renforce-Dynamics/beyondAMP": "humanoid",
    "YanjieZe/GMR": "humanoid",
    "limxdynamics/tron1-rl-isaaclab": "humanoid",
    "Mehooz/vision4leg": "quadruped",
    "nvidia-isaac/nvblox": "mapping",
    "gaiyi7788/awesome-legged-locomotion-learning": "resource",
    # 101-110
    "InternRobotics/InternNav": "nav",
    "allenzren/open-pi-zero": "vla",
    "PRIME-RL/SimpleVLA-RL": "vla",
    "OpenDriveLab/UniVLA": "vla",
    "toon-format/toon": "aicode",
    "Fission-AI/OpenSpec": "aicode",
    "deepinsight/insightface": "perception",
    "AnjieCheng/SpatialRGPT": "perception",
    "hovsg/HOV-SG": "mapping",
    "MCG-NJU/MixFormer": "perception",
    # 111-120
    "tud-amr/m3p2i-aip": "manip",
    "SJTU-ViSYS-team/Avoid-MPC": "uav",
    "NirAharon/BoT-SORT": "perception",
    "Ahmednull/L2CS-Net": "perception",
    "zylinzy/GazeHTA": "perception",
    "CMU-Perceptual-Computing-Lab/openpose": "perception",
    "HenryHuYu/DiffPhysDrone": "uav",
    "mikel-brostrom/boxmot": "perception",
    "onnx/onnx": "tools",
    "switchablenorms/DeepFashion2": "perception",
    # 121-130
    "PMY9527/QUAD-MPC-SIM-HW": "quadruped",
    "OpenQuadruped/spot_mini_mini": "quadruped",
    "felipemohr/IsaacLab-Quadruped-Tasks": "quadruped",
    "shaheenbharwani/sim2real-3d-printed-quadruped": "quadruped",
    "ARCaD-Lab-UM/RF-MPC": "quadruped",
    "datawhalechina/happy-llm": "resource",
    "datawhalechina/easy-rl": "resource",
    "Tian-Nian/control_your_robot": "manip",
    "mit-biomimetics/Cheetah-Software": "quadruped",
    "mike4192/spotMicro": "quadruped",
    # 131-140
    "chvmp/champ": "quadruped",
    "silvery107/rl-mpc-locomotion": "quadruped",
    "PetoiCamp/OpenCat-Quadruped-Robot": "quadruped",
    "gen-robot/RL4VLA": "vla",
    "RussTedrake/underactuated": "resource",
    "google-deepmind/mujoco_mpc": "tools",
    "zm0612/Hybrid_A_Star": "nav",
    "anassinator/ilqr": "tools",
    "simoninithomas/Deep_reinforcement_learning_Course": "resource",
    "ShangtongZhang/reinforcement-learning-an-introduction": "resource",
    # 141-150
    "udacity/deep-reinforcement-learning": "resource",
    "apple/ml-fastvlm": "perception",
    "MCZhi/Driving-IRL-NGSIM": "driving",
    "Tsinghua-MARS-Lab/StateTransformer": "rl",
    "ethz-asl/mav_voxblox_planning": "uav",
    "HKUST-Aerial-Robotics/Teach-Repeat-Replan": "uav",
    "ethz-asl/voxblox": "mapping",
    "HKUST-Aerial-Robotics/FIESTA": "uav",
    "niessner/VoxelHashing": "mapping",
    "ANYbotics/grid_map": "mapping",
    # 151-160
    "Lordog/dive-into-llms": "resource",
    "ZJU-FAST-Lab/Terrestrial-Aerial-Navigation": "nav",
    "CHH3213/chhRobotics_CPP": "resource",
    "Kedreamix/Awesome-Talking-Head-Synthesis": "resource",
    "ZJU-FAST-Lab/EVA-planner": "uav",
    "rongbohou/px4_fast_planner": "uav",
    "HKUST-Aerial-Robotics/EPSILON": "uav",
    "ApolloAuto/apollo": "driving",
    "eureka-research/DrEureka": "rl",
    "carla-simulator/carla": "driving",
    # 161-170
    "huangwl18/VoxPoser": "vla",
    "Arlo0o/StereoScene": "driving",
    "cyberbotics/webots": "sim",
    "THU-MIG/yolov10": "perception",
    "Factor-Robotics/Roller-Coaster-SLAM-Dataset": "slam",
    "MrNeRF/awesome-3D-gaussian-splatting": "resource",
    "AIDajiangtang/Superpoint-LightGlue-Image-Stiching": "perception",
    "apple/ml-hugs": "perception",
    "cvg/LightGlue": "perception",
    "vietanhdev/anylabeling": "tools",
    # 171-180
    "CVHub520/X-AnyLabeling": "tools",
    "nebula-beta/SLAM-Jobs": "resource",
    "i2Nav-WHU/OB_GINS": "vio_gnss",
    "yformer/EfficientSAM": "perception",
    "aau-cns/insane_dataset_tools": "vio_gnss",
    "JOP-Lee/READ": "driving",
    "SJTU-ViSYS/M2DGR": "vio_gnss",
    "weisongwen/UrbanLoco": "vio_gnss",
    "HKUST-Aerial-Robotics/gnss_comm": "vio_gnss",
    "XiaoyuShi97/FlowFormerPlusPlus": "perception",
    # 181-190
    "MCG-NKU/AMT": "perception",
    "drinkingcoder/FlowFormer-Official": "perception",
    "dachengxiaocheng/NDT-Transformer": "slam",
    "ov2slam/ov2slam": "slam",
    "geographiclib/geographiclib": "tools",
    "zhujun3753/i-octree": "mapping",
    "HKUST-Aerial-Robotics/GVINS-Dataset": "vio_gnss",
    "JiangboSong251/R2-GVIO": "vio_gnss",
    "LiZhengXiao99/Navigation-Learning": "resource",
    "tomojitakasu/RTKLIB": "vio_gnss",
    # 191-200
    "i2Nav-WHU/IC-GVINS": "vio_gnss",
    "JokerJohn/LIO_SAM_6AXIS": "slam",
    "HKUST-Aerial-Robotics/GVINS": "vio_gnss",
    "zm0612/eskf-gps-imu-fusion": "vio_gnss",
    "ydsf16/imu_gps_localization": "vio_gnss",
    "MichaelGrupp/evo": "tools",
    "IRVING-L/Algorithm_fromBilibili": "resource",
    "JingwenWang95/DSP-SLAM": "slam",
    "princeton-vl/RAFT-Stereo": "perception",
    "boxuLibrary/drt-vio-init": "vio_gnss",
    # 201-210
    "dzunigan/imu_initialization": "vio_gnss",
    "zju3dv/vig-init": "vio_gnss",
    "symao/vio_evaluation": "vio_gnss",
    "Cc19245/LVI-SAM-Easyused": "slam",
    "TixiaoShan/LVI-SAM": "slam",
    "HKUST-Aerial-Robotics/VINS-Fusion": "slam",
    "zinuok/VINS-Fusion-ROS2": "slam",
    "ros/meta-ros": "ros",
    "realsenseai/meta-intel-realsense": "ros",
    "balloonwj/CppGuide": "resource",
    # 211-220
    "zhouyong1234/SLAM-All-In-One": "resource",
    "Ly0n/awesome-robotic-tooling": "resource",
    "ethz-asl/kalibr": "vio_gnss",
    "OctoMap/octomap": "mapping",
    "Ewenwan/ORB_SLAM2_SSD_Semantic": "slam",
    "lturing/ORB_SLAM3_FAST_IMU_INIT": "slam",
    "aipiano/guided-filter-point-cloud-denoise": "perception",
    "UCR-Robotics/Citrus-Farm-Dataset": "vio_gnss",
    "mlabonne/llm-course": "resource",
    "CruxDevStuff/allan_ros2": "vio_gnss",
    # 221-230
    "Ewenwan/MVision": "resource",
    "LeonardoDiCaprio1/Map_ORBSLAM_ROS": "slam",
    "cpymaple/ORB-SLAM3-YOLOv3": "slam",
    "SlamMate/CDS-SLAM-Semantic-mapping-in-dynamic-environment": "slam",
    "Light-City/CPlusPlusThings": "resource",
    "ros-drivers/usb_cam": "ros",
    "EndlessLoops/ORB_SLAM3_ROS2": "slam",
    "zang09/ORB-SLAM3-STEREO-FIXED": "slam",
    "introlab/rtabmap": "slam",
    "monemati/PX4-ROS2-Gazebo-YOLOv8": "uav",
    # 231-242
    "ZJU-FAST-Lab/ego-planner": "uav",
    "UZ-SLAMLab/ORB_SLAM3": "slam",
    "ARK-Electronics/ROS2_PX4_Offboard_Example": "uav",
    "zang09/ORB_SLAM3_ROS2": "slam",
    "guanboang/PoloMan": "other",
    "ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code": "resource",
    "google-research/tuning_playbook": "resource",
    "moyuweiqing/A-stock-prediction-algorithm-based-on-machine-learning": "timeseries",
    "yangwohenmai/TimeSeriesForecasting": "timeseries",
    "yangwohenmai/LSTM": "timeseries",
    "Ewenwan/UCL-DeepReinforcementLearning": "resource",
    "kaieye/2022-Machine-Learning-Specialization": "resource",
}


def gh_anchor(text: str) -> str:
    """复刻 GitHub 的 heading anchor 生成规则：
    - 小写化
    - 字母 / 数字 / Mark(变体选择符等) / '-' / '_' / '.' 保留
    - 空格变 '-'
    - 其他（标点、emoji 等）全部丢弃
    """
    out = []
    for c in text.lower():
        if c.isspace():
            out.append("-")
        elif c in "-_.":
            out.append(c)
        else:
            cat = unicodedata.category(c)
            if cat[0] in ("L", "N", "M"):  # Letter / Number / Mark
                out.append(c)
    return "".join(out)


def main():
    repos = []
    with META.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            repos.append(d)

    buckets = defaultdict(list)
    missing = []
    for r in repos:
        name = r["full_name"]
        cat = M.get(name)
        if cat is None:
            missing.append(name)
            cat = "other"
        buckets[cat].append(r)

    lines = []
    lines.append("# GitHub Stars 分类汇总")
    lines.append("")
    lines.append(f"共 **{len(repos)}** 个 starred 仓库，按主题归类如下。")
    lines.append("")

    # 目录
    lines.append("## 目录")
    lines.append("")
    for key, title in CATEGORIES:
        n = len(buckets.get(key, []))
        if n:
            anchor = gh_anchor(title)
            lines.append(f"- [{title}](#{anchor}) — {n} 项")
    lines.append("")

    # 各分类详情
    for key, title in CATEGORIES:
        items = buckets.get(key, [])
        if not items:
            continue
        lines.append(f"## {title}")
        lines.append(f"*({len(items)} 项)*")
        lines.append("")
        for r in sorted(items, key=lambda x: x["full_name"].lower()):
            name = r["full_name"]
            url = r.get("url") or f"https://github.com/{name}"
            desc = (r.get("description") or "(无描述)").strip()
            lang = r.get("language") or "—"
            topics = r.get("topics") or []
            tstr = f"  `#{'` `#'.join(topics)}`" if topics else ""
            lines.append(f"- **[{name}]({url})** · `{lang}` — {desc}{tstr}")
        lines.append("")

    if missing:
        lines.append("## ⚠️ 未在映射表中的仓库（已落到 other）")
        for m in missing:
            lines.append(f"- {m}")
        lines.append("")

    OUT.write_text("\n".join(lines))
    print(f"wrote {OUT}, total={len(repos)}, missing={len(missing)}")
    if missing:
        for m in missing:
            print(f"  MISSING: {m}")


if __name__ == "__main__":
    main()
