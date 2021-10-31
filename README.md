# READ BEFORE PROCEED

## Big Sur (aka Big Nuissance) Build

This repository contain necessary edits made to the original ORB-SLAM3 library in order to build on a Apple M1 machine running on macOS Big Sur.

These edits are:

1. Remove OpenCV 4.0 dependency in CMakeLists.txt
2. Trim off "-march=native" in CMakeLists.txt
3. Install boost
4. export OpenCV_DIR=/opt/local/libexec/opencv3/cmake/
5. export LD_LIBRARY_PATH=/opt/local/libexec/boost/1.76/include/boost
6. /Users/maclaptop/Desktop/UCLA/2021-2022/ORB_SLAM3/Thirdparty/DBoW2/DBoW2/FORB.cpp:16:10: fatal error: 'stdint-gcc.h' file not found
7. /Users/maclaptop/Desktop/UCLA/2021-2022/ORB_SLAM3/Thirdparty/DBoW2/DBoW2/BowVector.h:17:10: fatal error: 'boost/serialization/serialization.hpp' file not found → add -I/opt/local/libexec/boost/1.76/include to CMakeLists.txt
8. Remove "tr1" in these files:
    1. g2o/g2o/core/robust_kernel.h
    2. g2o/g2o/core/hyper_graph.h
    3. g2o/g2o/core/sparse_block_matrix_ccs.h
    4. g2o/g2o/core/sparse_block_matrix.hpp
    5. g2o/g2o/core/marginal_covariance_cholesky.h
9. ORB_SLAM3/include/Map.h: GLubyte* mThumbnail; →  unsigned char* mThumbnail;
10. ORB_SLAM3/include/MapDrawer.h add #include<pangolin/display/opengl_render_state.h>
11. ORB_SLAM3/src/ORBmatcher.cc #include<stdint-gcc.h> → #include<stdint.h>
12. ORB_SLAM3/src/Map.cc GLubyte → unsigned char
13. ORB_SLAM3/src/MapDrawer.cc add #include <pangolin/gl/glstate.h>
14. ORB_SLAM3/src/Viewer.cc add #include <pangolin/display/display.h>
15. same file #include <pangolin/display/attach.h>
16. same file #include <pangolin/display/widget/widgets.h>
17. ORB_SLAM3/src/System.cc add #include <pangolin/display/display.h>
18. comment out occurrences of GL_RGBA32F or change it to GL_RGBA and GL_RGB32F to GL_RGB in:
    1. pangolin/gl/gl.hpp
    2. pangolin/gl/glpixformat.h
19. ThirdParty/DWoB/CMakeLists.txt remove OpenCV 4.0
20. Change CMakeLists.txt as https://github.com/raulmur/ORB_SLAM2/issues/94 suggests
21. Add these to CMakeLists.txt target_link_libraries
    1. ${PROJECT_SOURCE_DIR}/Thirdparty/DBoW2/lib/libDBoW2.dylib
    2. ${PROJECT_SOURCE_DIR}/Thirdparty/g2o/lib/libg2o.dylib
    3. -L/opt/local/libexec/boost/1.76/lib
    4. -lboost_serialization-mt
    5. -L/opt/local/lib
    6. -lcrypto
    7. -lpangolin
22. /opt/local/include add to CMakeLists.txt include_directories
23. Use Pangolin 0.6
24. System.cc add @ line 377:
    1. void System::RunViewer()
    2. {
    3.     mpViewer->Run();
    4. }
25. System.h remove std::thread* mptViewer;
26. System.h add void RunViewer(); @ line 119
27. Examples/Monocular/mono_euroc.cc Examples/Monocular/mono_kitti.cc Examples/Monocular/mono_tum.cc Examples/RGB-D/rgbd_tum.cc Examples/Stereo/stereo_euroc.cc Examples/Stereo/stereo_kitti.cc
    1. Do anything mentioned in https://github.com/raulmur/ORB_SLAM2/pull/179/files except for the sleep thingy BUT
    2. Use int processing(int argc, char **argv, ORB_SLAM3::System *slamPtr); because function "processing" needs "argc" and "ORB_SLAM3" namespace instead of "ORB_SLAM2"

## Compilation

```
git clone https://github.com/Estorva/ORB-SLAM3-BigSur.git ORB_SLAM3
cd ORB_SLAM3
chmod +x ./build.sh
./build.sh
```

__*Make sure these prerequisites are met:*__

+ Library ```boost``` is installed.
+ Have ```opencv3``` installed and type ```export OpenCV_DIR=/opt/local/libexec/opencv3/cmake/``` in terminal
+ ```glew``` and ```glfw``` are installed
+ ```Pangolin``` is built and its libraries can be found somewhere the flag ```-L``` passed to compiler covers.

The original README.md can be found at: https://github.com/UZ-SLAMLab/ORB_SLAM3
