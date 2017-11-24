import boto.ec2
import time
import os 

#global string varaiables 
Security_Group_Name = 'csc326-group7' 
Image_ID= 'ami-8caa1ce4'
Key_Pair_Name = 'keypair'

AWS_Access_Keyid= 'AKIAJJW55HSKRY6H24IA'
  # key_id  and security key of the user built in AWS 
AWS_Access_Securitykey='G4Ps6gyEH8Ixet++zcZXCgN/Eh8Rn1q2Q2Av6Km9' 

# start a new connection to region us-east-1 
connection = boto.ec2.connect_to_region('us-east-1',aws_access_key_id = AWS_Access_Keyid,aws_secret_access_key =AWS_Access_Securitykey) 

#create key-pair

KeyPair = connection.create_key_pair('key_pair_name')
KeyPair.save('./')

#Establish a new security group
Security_Group = connection.create_security_group(name='csc326-group7' , description='security group eastablished for lab2') 

#create authorization for the 3 ports:

Security_Group.authorize('ICMP',-1,-1,'0.0.0.0/0') 
# allows icmp ping packet to come in 
Security_Group.authorize('TCP',22,22,'0.0.0.0/0') 
# allows SSH server to connect 
Security_Group.authorize('TCP',80,80,'0.0.0.0/0')
# allows HTTP server to connect 


# create a new instance with the given parameter 
reservation_objblock = connection.run_instances(            image_id = 'ami-8caa1ce4',    
                                                            key_name = 'key_pair_name',   
                                                            instance_type='t1.micro',
                                                            security_groups=['csc326-group7']
                                       )   
new_instance = reservation_objblock .instances[0]   # esatablis the new instance to live 

#new_instance.update() 


while (new_instance.update()!='running'):    #using a while loop to wait until the instance is at "running" state 
    time.sleep(5)                            # or sleep to add on some time delay  
    
#print('ready to stablize ip address') 

#stablize elastic ip address and asscociate it with the instance 
stable_IP= connection.allocate_address()
stable_IP.associate(instance_id = new_instance.id) 

#print(stable_IP)
# print out the elastic ip address just for future use 
#34.237.28.99







