from text_to_image import text_to_image_fitting

email_dict = {
    'David Srolovitz' : 'srol@hku.hk',
    'Jian Han' : 'jianhan@cityu.edu.hk',
    'Subrahmanyam Pattamatta' : 'psmanyam@hku.hk',
    'Tongqi Wen' : 'tongqwen@hku.hk',
    'Zhuoyuan Li' : 'zhuoyli@connect.hku.hk',
    'Zhizi Guan' : 'zhiziguan@connect.hku.hk',
    'Xiaoguo Gong' : 'gongxg@connect.hku.hk',
    'Beilin Ye' : 'beilinye@connect.hku.hk',
    'Anwen Liu' : 'anwenliu2-c@my.cityu.edu.hk',
    'Jinxin Yu' : 'jinxinyu2-c@my.cityu.edu',
    'Jing Fang' : 'jingfang9-c@my.cityu.edu.hk',
    'Zhaowei Wang': 'zhaowwang2-c@my.cityu.edu.hk',
    'Dongsong Tao': 'dongsotao2-c@my.cityu.edu.hk',
    'Caihao Qiu' : 'caihaoqiu2-c@my.cityu.edu.hk',
    'Siqi Wang' : 'swang347-c@my.cityu.edu.hk',
    'Zichen Song' : 'alansong641@163.com',
    'Simeon Ristic' : 'sristic@seas.upenn.edu',
    'Larissa Woryk' : 'lworyk@seas.upenn.edu',
    'Han Liu' : 'hliu238-c@my.cityu.edu.hk',
    'Avatar X' : 'avatarX@abc.edu'
}

for name, email in email_dict.items():

    filename = name.lower()
    filename = '../group/emails/' + filename.replace(' ', '_') + '.png'
    text_to_image_fitting(email, filename)
