import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler

def create_waypoints():
  side = float(input("Enter the side length (less than 3.5): ")) #accept side length of the square
  repeat = int(input("Enter the number of times to repeat the sequence: ")) # accept the number of times to repeat

  if side >= 3.5: # set a maximum limit on the side length of the square
    side = 3.5 
  
  points = [(side/2, side/2), (side/2, -side/2), (-side/2, -side/2), (-side/2, side/2)] #set the coordinates
  yaw_euler = [(0.0, -0.0, 4.71238898038469), (0.0, -0.0, 3.141592653589793), (0.0, -0.0, 1.5707963267948966), (0.0, -0.0, 0.0)]
  # set the yaw angles as roll pitch and yaw (euler form) in radians

  yaw_quaternion = []
  for i in yaw_euler:
    yaw_quaternion.append(quaternion_from_euler(i[0], i[1], i[2])) # convert them into quaternions from euler form
  
  waypoints = {"position sequence": points, "orientation sequence": yaw_quaternion, "repeat": repeat}
  return waypoints # return a dictionary with sequence pose data as well as the number of times to repeat  

def movebase_client(px, py, oz, ow):

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = px
    goal.target_pose.pose.position.y = py
    goal.target_pose.pose.orientation.z = oz
    goal.target_pose.pose.orientation.w = ow

    client.send_goal(goal)
    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Action server not available.")
        rospy.signal_shutdown("Action server not available.")
    else:
        return client.get_result()

if __name__ == '__main__':
  waypoints = create_waypoints()
  
  for i in range(0, waypoints['repeat']):
    try:
      for j in range(0, len(waypoints['position sequence'])):
        rospy.init_node('movebase_client_py')
        result = movebase_client(waypoints['position sequence'][j][0], waypoints['position sequence'][j][1], waypoints['orientation sequence'][j][2], waypoints['orientation sequence'][j][3])
        if result:
          rospy.loginfo("Point " + str(j + 1) + " done in square " + str(i + 1) + " of " + str(waypoints['repeat']))
    except rospy.ROSInterruptException:
      rospy.loginfo("Navigation completed.")