let Mock = require('mockjs')

let data = Mock.mock({
    'list|1-10': [{
        'id|+1': 1
    }],
    "string|1-10": "★",
    "boolean|1": true,
    "object|2": {
        "310000": "上海市",
        "320000": "江苏省",
        "330000": "浙江省",
        "340000": "安徽省"
    },
    'regexp|1-5': /\d{5,10}\-/


})

console.log(JSON.stringify(data, null, 4))
