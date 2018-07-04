from faker import Faker
fake = Faker(locale="zh_CN")
print(fake.name())
print(fake.address())
# https://github.com/joke2k/faker