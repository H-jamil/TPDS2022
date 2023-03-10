import subprocess
from datetime import datetime
import csv
import time

#
			# 13 SHARED PARAMETERS (0 - 12)
            #--------------------------------
			# 0. Testbed: name of testbed either Chameleon or CloudLab
		 	# 1. algName: name of algorithm
		 	# 2. htmlCount: how many files from html dataset
		 	# 3. imageCount: how many files from image dataset
		 	# 4. videoCount: how many files from video dataset
		 	# 5. serverIP
		 	# 6. port
		 	# 7. bandwidth: in Mbps
		 	# 8. RTT: in ms
		 	# 9. TCPMaxBuf: in MB
		 	# 10. Max Channels
		 	# 11 Alg Interval
		 	# 12. outputLog --> after completing transfer (Writes the Average Throughput)
		 	# *****************************************************************************
		 	# PARAMETERS SPECIFIC TO TEST DECISION TREE (13 -
		 	# 13. Initial Alg Interval - 1st alg interval (sampling) in seconds. Used for inittial parameters
		 	# 14. Name of Decision Tree Instantaneous Output Log File - Written instantaneously to to file at regular intervals
		 	# 15. DecisionTreeHashTable FileName and Path
		 	# 16. DecisionTreeHashTable Size: Different for Testbed, datatype combination
		 	# 17. totalNumPhysicalCores
		 	# 18. totalNumLogicalCores
            # 19. MinRttInterval
            # 20. MaxRttInterval

for i in range(2):
    #Decision Tree - HTML
    cmd_prefix = 'sudo java -d64 -Xms15g -Xmx15g -XX:MaxDirectMemorySize=50G -cp .:lib/*:bin/'
    testBedName = 'cloudlab'
    # algorithm = 'testDecisionTree'
    algorithm='testWebServer'
    # dataset = NUM HTML FILES, NUM IMAGE FILES, NUM VIDEO FILES
    HTML_dataset = '20000 0 0'  # HTML: 20000 FILES, IMAGE:0 FILES, VIDEO: 0 Files
    medium_dataset = '0 5000 0'  # HTML:0 FILES, IMAGE: 5000 FILES, VIDEO: 0 Files
    large_dataset = '0 0 128'  # HTML:0 FILES, IMAGE:0 FILES, VIDEO: 128 Files
    server_ip = '128.105.145.216'
    bandwidth = '1000'  # Mbps
    rtt = '36'  # ms
    tcp_buf = '4.5'  # MB
    max_channels = '32'
    alg_interval = '30'  # Seconds
    output_log = 'output/CloudLab_testWebServer_Avg_Data_Transfer_Dec_28_2022.csv'
    init_alg_interval = '10'  # Seconds
    inst_d_tree_output_log = '/mnt/ramdisk/testWebServer_cloudlab_InstLog.csv'
    decisionTreeHashTableName = "input/D_Tree_HashFiles/CloudLab/CloudLab_Image_D_Tree_Hash_File.csv"
    decisionTreeHashTableSize = '120'
    totalNumPhysicalCores = '10'
    totalNumLogicalCores = '20'
    governor = 'userspace'

    dataset = medium_dataset

    cmd = cmd_prefix + ' ' + \
          'algorithms.OptimalDataTransfer' + ' ' + \
          testBedName + ' ' + \
          algorithm + ' ' + \
          dataset + ' ' + \
          server_ip + ' ' + \
          str(80) + ' ' + \
          bandwidth + ' ' + \
          rtt + ' ' + \
          tcp_buf + ' ' + \
          max_channels + ' ' + \
          alg_interval + ' ' + \
          output_log + ' ' + \
          init_alg_interval + ' ' + \
          inst_d_tree_output_log + ' ' + \
          decisionTreeHashTableName + ' ' + \
          decisionTreeHashTableSize + ' ' + \
          totalNumPhysicalCores + ' ' + \
          totalNumLogicalCores + ' ' + \
          governor
    print('Start transfer: Test CloudLab,  Iteration: ' + ", Dataset = " + dataset)
    subprocess.run(cmd, shell=True)
    print('Finished transfer of: Test CloudLab,  Iteration: ' + ", Dataset = " + dataset)
    time.sleep(10)


