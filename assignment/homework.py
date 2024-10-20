import pandas as pd


class StudentDatabase:
    def __init__(self, filepath):
        # 使用GBK编码读取CSV文件
        self.data = pd.read_csv(filepath, encoding='GBK')

    def find_students(self, student_id=None, name=None, grade=None):
        # 基于提供的参数构建查询条件
        query = {}
        if student_id is not None:
            query['学号'] = student_id
        if name is not None:
            query['姓名'] = name
        if grade is not None:
            query['成绩'] = grade

        # 根据构建的查询条件进行查询
        result = self.data
        for key, value in query.items():
            result = result[result[key] == value]
        return result

    def verify_entry(self, student_id, name, grade):
        # 验证完整的学生记录是否存在
        result = self.find_students(student_id=student_id, name=name, grade=grade)
        return not result.empty


# 示例：创建数据库实例并查询
db = StudentDatabase('data.csv')  # 将 'path_to_your_data.csv' 替换成你的CSV文件路径
result = db.find_students(student_id=20240001)
print(result)
