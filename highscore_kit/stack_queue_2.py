import math 


progresses= [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# day_list = []
# launch_list = []





# def launch_days():
#     launch = 0
#     d = count_days(p, s)
    
#     for i in d:
#         if launch < i:
#             launch = i
#         else:
#             i = launch                         
#         launch_list.append(i)

#     return launch_list

# def check_duplicate():
#     list = launch_days()
   
#     count_list = []
#     seen = set()

#     for num in list:
#         if num not in seen:
#             count = list.count(num)
#             count_list.append(count)
#             seen.add(num)


#     print(count_list)
        

# check_duplicate()

    
# count_d = count_days(p, s)
# print(count_d)    
# launch = launch_days()
# print(launch)


def solution(progresses, speeds):
    day_list = []
    launch_list = []

    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i])/speeds[i])
        day_list.append(day)
    
    launch = 0
    
    for i in day_list:
        if launch < i:
            launch = i
        else:
            i = launch                         
        launch_list.append(i)
   
    answer = []
    seen = set()

    for num in launch_list:
        if num not in seen:
            count = launch_list.count(num)
            answer.append(count)
            seen.add(num)


    return answer

a = solution(progresses, speeds)
print(a)