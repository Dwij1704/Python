def teams():
    total_teams=int(input("Enter Total number of teams (usually 5-7): "))
    teams={}
    scores={}
    win={}
    tie={}
    points={}
    avg={}
    board={}
    k=0
    for i in range(1,total_teams+1):
        teams[i]=input("Enter name for team number "+str(i)+": ")
    for i in range(1,total_teams+1):
        win[i]=0
        avg[i]=[]
        board[i]=0
        scores[i]=[0]
        points[i]=[]
        tie[i]=0
    for i in range(1,total_teams+1):
        for j in range(i+1,total_teams+1):
            k+=1
            print("Match",k,": ",teams.get(i),"Vs",teams.get(j),"\nScore")
            
            score1=input(str(teams.get(i)+": "))
            while not str(score1).isdigit()or int(score1)<0:
                print("Enter Valid score:")
                score1=input(str(teams.get(i)+": "))
            
            score2=input(str(teams.get(j)+": "))
            while not str(score2).isdigit():
                print("Enter Valid score:")
                score2=input(str(teams.get(j)+": "))
            score1=int(score1)
            score2=int(score2)
            if score1>score2:
                win[i]+=1
                scores[i].append(score1)
            elif score1==score2:
                scores[i].append(score1)
                scores[j].append(score2)
                tie[i]+=1
                tie[j]+=1
            else:
                win[j]+=1
                scores[j].append(score2)
    print(scores)
    for k,v in scores.items():
        if len(v)-1!=0:
            avg[k]=sum(v)/(len(v)-1)
        else:
            avg[k]=0
    print(avg)
    print(win)
    print(tie)
    for k,v in win.items():
        points[k]=v*4
    for k,v in tie.items():
        points[k]=points[k]+(v*1)
    print(points)
    asc_points=dict(sorted(points.items(), key=lambda x: x[1],reverse=True))
    # print(asc_points)
    # count=1
    # for i,j in asc_points.items():
    #     for k,v in asc_points.items():
    #         if k!=i:
    #             if j==v:
    #                 if avg[i]<avg[k]:
    #                     board[count]=k
    #                 else:
    #                     board[count]=i
    #             else:
    #                 board[count]=i
    #     count+=1
    # print(board)
    # print("Final Score Board:-")
    # for k,v in board.items():
    #     print(teams[v],points[v])
    print("Final Score Board:-")
    for k,v in asc_points.items():
        print(teams[k])
teams()