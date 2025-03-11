#include <ros/ros.h>
#include <std_msgs/String.h>

void callback(const std_msgs::String::ConstPtr& msg, const std::string& topic_name) {
    ROS_INFO("Received from %s: %s", topic_name.c_str(), msg->data.c_str());
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "multi_topic_subscriber");
    ros::NodeHandle nh;

    std::vector<ros::Subscriber> subscribers;
    for (int i = 0; i < 10; ++i) {
        std::string topic = "/topic_" + std::to_string(i);
        nh.subscribe<std_msgs::String>(topic, 10, boost::bind(callback, _1, topic));
    }

    ros::spin();
    return 0;
}
