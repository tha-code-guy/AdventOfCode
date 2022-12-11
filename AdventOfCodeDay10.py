while True:         
        cycle=1
        x=1
        instructionsin=[]
        pairite=True
        import sys
        temp=""
        print("Hey,past the input and on a new line press 'ctrl+z' and hit 'enter' to start.  ")
        instructions=(sys.stdin.readlines())
        pathway={1:1}

        for i in range(len(instructions)):
            if instructions[i][0]=="n":
                                cycle+=1
                                pathway[cycle]=x
            elif instructions[i][0]=="a":
                                cycle+=1
                                pathway[cycle]=x
                                cycle+=1
                                pathway[cycle]=x
            for j in range(5,len(instructions[i])):
                            
                                if instructions[i][j]=="-":
                                                    pairite=False
                                elif  instructions[i][j].isdigit():
                                        temp+=instructions[i][j]  
                            
                                # if (instructions[i][7].isdigit()):
                                #     temp+=int(instructions[i][7]) 
            if temp.isdigit():                    
                        temp=int(temp) 
                                
                        if pairite==False:
                            temp*=-1
                            pairite=True
                        
                        x+=temp
                        pathway[cycle]=x
                        temp=""
                                                
                                
        print("During the {1}th cycle, register X has the value {0}, so the signal strength is ,{1}*{0} ={2}".format(pathway.get(20),str(20),str(int(pathway.get(20))*20)))
        print("During the {1}th cycle, register X has the value {0}, so the signal strength is ,{1}*{0} ={2}".format(pathway.get(60),str(60),str(int(pathway.get(60))*60)))  
        print("During the {1}th cycle, register X has the value {0}, so the signal strength is ,{1}*{0} ={2}".format(pathway.get(100),str(100),str(int(pathway.get(100))*100)))  
        print("During the {1}th cycle, register X has the value {0}, so the signal strength is ,{1}*{0} ={2}".format(pathway.get(140),str(140),str(int(pathway.get(140))*140)))  
        print("During the {1}th cycle, register X has the value {0}, so the signal strength is ,{1}*{0} ={2}".format(pathway.get(180),str(180),str(int(pathway.get(180))*180)))  
        print("During the {1}th cycle, register X has the value {0}, so the signal strength is ,{1}*{0} ={2}".format(pathway.get(220),str(220),str(int(pathway.get(220))*220))) 
        sum=int(pathway.get(20))*20+int(pathway.get(60))*60+int(pathway.get(100))*100+int(pathway.get(140))*140 +int(pathway.get(180))*180+int(pathway.get(220))*220
        print("The sum of these signal strengths is {0}.".format(sum)) 
                                    
                    



