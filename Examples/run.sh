#!/bin/bash
pathDatasetEuroc='/Users/maclaptop/Desktop/UCLA/2021-2022/ORB_SLAM3/Examples/Datasets/EuRoC' #Example, it is necesary to change it by the dataset path
#SLAM="./Monocular/mono_euroc"
SLAM="./Monocular/mono_euroc"
VOC="../Vocabulary/ORBvoc.txt"
CONFIG="./Monocular/EuRoC_1.yaml"
DATASET="./Datasets/EuRoC_1"
TIMESTAMP="./Datasets/EuRoC_1/timestamps.txt"
OUTPUT_IDENT="result_EuRoC_1"

# Single Session Example (Pure visual)
echo "Launching MH01 with Monocular sensor"
#./Stereo/stereo_euroc ../Vocabulary/ORBvoc.txt ./Stereo/EuRoC.yaml "$pathDatasetEuroc"/MH01 ./Stereo/EuRoC_TimeStamps/MH01.txt dataset-MH01_stereo
# Usage: ./stereo_euroc
#   path_to_vocabulary
#   path_to_settings
#   path_to_sequence_folder_1
#   path_to_times_file_1
#   (path_to_image_folder_2 path_to_times_file_2 ... path_to_image_folder_N path_to_times_file_N)
#   trajectory_file_name
${SLAM} ${VOC} ${CONFIG} ${DATASET}/MH01 ${TIMESTAMP} ${OUTPUT_IDENT}
#echo "------------------------------------"
#echo "Evaluation of MH01 trajectory with Stereo sensor"
#python2 ../evaluation/evaluate_ate_scale.py ../evaluation/Ground_truth/EuRoC_left_cam/MH01_GT.txt f_dataset-MH01_stereo.txt --plot MH01_stereo.pdf
