#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class PubSubNode:
    def __init__(self):
        rospy.init_node("pubsub_node", anonymous=True)

        self.publisher = rospy.Publisher("talking_topic_2", String, queue_size=10)
        rospy.Subscriber("talking_topic", String, self.callback)

    def decrypt_caesar_cipher(self, text, shift):
        decrypted_text = ""

        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = chr((ord(char) - ord('A' if is_upper else 'a') - shift) % 26 + ord('A' if is_upper else 'a'))

            decrypted_text += char

        return decrypted_text

    def callback(self, data):
        encrypted_name = data.data
        shift_value = 3 

        decrypted_name = self.decrypt_caesar_cipher(encrypted_name, shift_value)
        rospy.loginfo("Received and decrypted data: %s", decrypted_name)

        self.publisher.publish(decrypted_name)

    def run(self):
        rospy.loginfo("PubSubNode started ...")
        rospy.spin()
        

if __name__ == "__main__":
    try:
        node = PubSubNode()
        node.run()
    except rospy.ROSInterruptException:
        pass
