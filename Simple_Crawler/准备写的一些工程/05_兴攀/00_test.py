import json

data = {
    'code': 1000,
    'message': '操作成功',
    'request_url': '/treemp/tree.Tasks/receiveTaskReward',
    'success': True,
    'data': {
        'reward': [
            {
                'id': 31,
                'day_task_id': 13,
                'task_type': 0,
                'reward_probability': 0,
                'reward_type': 2,
                'reward': 10,
                'coupon_id': 0,
                'img_id': None,
                'is_delete': 0,
                'create_time': None,
                'update_time': '2023-07-0511: 47: 43',
                'reward_type_name': '肥料'
            }
        ]
    }
}

# data = json.dumps(data)
print(data["data"]["reward"][0]["reward_type_name"])


