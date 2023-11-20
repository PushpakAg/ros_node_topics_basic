#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
        encrypted_text += char

    return encrypted_text

def talking_pub():
    pub = rospy.Publisher("talking_topic", String, queue_size=10)
    rospy.init_node("publisher_node", anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher node started and started publishing")
    
    name = "Pushpak" 
    shift_value = 3   

    while not rospy.is_shutdown():
        encrypted_name = encrypt_caesar_cipher(name, shift_value)
        pub.publish(encrypted_name)
        rate.sleep()

if __name__ == "__main__":
    try:
        talking_pub()
    except rospy.ROSInterruptException:
        pass
