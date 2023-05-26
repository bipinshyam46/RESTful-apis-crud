import requests

# response=requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
# # print(response.json()['items'])

# for data in response.json()['items']:
#     if data['answer_count']==1:
#         print(data['title'])
#     else:
#         print('Skipped')
#     print()