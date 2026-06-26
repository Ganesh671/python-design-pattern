
from builderPattern import  FundsBuilder


def test_builder():
    build = FundsBuilder() \
            .addId(1)\
            .addname("Apple") \
            .addPrice(2000) \
            .build()
    assert(build.name == "Apple")

def test_builder2():
    build = FundsBuilder() \
            .addId(2)\
            .addname("Apple") \
            .addPrice(2500) \
            .build()
    assert(build.name == "Apple")


test_builder()
test_builder2()