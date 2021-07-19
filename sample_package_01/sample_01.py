from sample_package_01 import module_01, module_02
from sample_package_01.module_01 import Person, func1, num
from sample_package_01.module_02 import size

# 시작점 지정
if __name__ == '__main__':
    print(module_01.num)
    module_01.func1()
    p = module_01.Person()

    print(module_02.size)

    print(num)
    func1()
    p = Person()

    print(size)
