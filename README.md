# 6-DOF Monocular SLAM-Based Wearable\\Eye-Gaze Tracker with Inertial Tracking

### Summary:
Wearable eye-gaze platforms allow users to track their gaze in an environment governed by an real-view camera, but does not provide depth information. By integrating monocular SLAM into wearable eye-gaze technology, we obtain 6-DOF information of the user and get features of the gaze that relate to the depth of the user's view.

### Splash images
![Figure 1](/assets/images/fig1.jpg) 
![Figure 2](/assets/images/fig2.jpg)

### Project git repo(s):
[https://github.com/therhetoricalcow/Wearable_Eye_SLAM](https://github.com/therhetoricalcow/Wearable_Eye_SLAM)

## Big picture 

### What is the overall problem that this and related research is trying to solve?
Predicting gaze is a problem that has been tackled over the last 20 years, but most modern state-of-the-art gaze trackers rely on predicting gaze position onto a 2-Dimensional Location. In use cases such as neurology and Augmented Reality (AR), users would want to know how far a particular object is from them while stationary and when moving. Satellite-based GPS cannot assist with localization due to the large extent of distance error (10-15 meters). Our research solves this by incorporating a precise and low-cost mapping solution that localizes the user.  It will be able to determine not just where the user is looking at but also the object (in a three-dimensional mapping) at which they are looking. This works by first mapping the environment with a custom-monocular wearable eye-tracker and then performing localization using a combination of 3-D mapping based on a platform such as ORB3, the head pose attained from Inertial Measuring Units (IMUs), and the user's gaze determined from an eye-tracking system.  

### Why should people (everyone) care about the problem?
This problem is relevant to modern-day applications of eye-tracking wearables since it translates from using outside-in tracking to inside-out tracking. Current inside-out tracking devices rely on binocular tracking methods, but we intend to make this possible using monocular SLAM, hence decreasing the cost and weight of the mechanism.  

### What has been done so far to address this problem?
Tobii's Pico Neo 2 Eye and Vive Pro Eye utilizes inside-out tracking but with binocular environmental cameras. Pupil Labs has an environment camera but maps the gaze direction to a corresponding position in an environmental 2-D Image.  

## Specific project scope

### What subset of the overall big picture problem are you addressing in particular?
We want to see the effectiveness and performance of using Monocular SLAM with different eye-tracking methods.  

### How does solving this subproblem lead towards solving the big picture problem?
This solution allows for a more cost-effective approach at fusing eye-tracking with slam. Current Headsets use binocular for tracking but Monocular Based Methods are not used.  

### What is your specific approach to solving this subproblem?
ORB3-SlAM will be used to implement SLAM onto a Monocular Fish-Eye Camera, the IMU can return the result as a Quaternion and can be fused with the SLAM solution. Gaze Tracking can be done with 2 Near Infrared Webcams that either use Edge-Based Machine Learning or Feature-Based Ellipse Fitting to Figure out Pupil Ellipsing.  

### How can you be reasonably sure this approach will result in a solution?
The ORB3-Slam will allow for some sort of Indoor Mapping. By using a variety of fusion and calibration practices, we can determine the effectiveness of Monocular Indoor Slam for Eye Tracking By determining gaze effectiveness at different distances.  

### How will we know that this subproblem has been satisfactorily solved, using quantitative metrics?
By observing the root-mean square error of perceived gaze and true gaze upon different features picked out by the SLAM, we can use quantitative metrics to determine the accuracy and statistics behind the setup.  

## Broader impact

### What is the value of your approach beyond this specific solution?
This allows for the Field of Neurology and AR/VR Solutions to be incentized to try more cost effective solutions with high-accuracy. It allows for a custom 6-DOF headset that is not commercialized but can be open-sourced. It is more cost effective as it explores the usage of a wide angle single camera rather an assortment of different cameras.  

### What is the value of this solution beyond solely solving this subproblem and getting us closer to solving the big picture problem?
This solution allows for us to evaluate SOTA Monocular SLAM Methods for Usages in Eye-Tracking. Current SLAM Methods for Monocular Indoor Tracking are considered fairly accurate but have nebever been explored to evaluate the accracy of determining gaze position.  

## Background / related work / references

## System capabilities, validation deliverables, engineering tasks

### Concrete external deadlines (paper submissions):
We need to prepare a teaser by Week 9, a presentation by Week 10, and a final paper by Week 10.  

### Detailed schedule (weekly capabilities / deliverables / tasks):
