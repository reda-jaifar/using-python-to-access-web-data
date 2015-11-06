import re

data = "from mr.jaifar@gmail.com Sat Jan 31 10:15:18 2013"


def find_all():
    y = re.findall('\S+@\S+', data)
    print y


# Extracting the domain name using find and String slicing
def find_domain_name():
    domain_name = re.findall('^from .*@([^ ]*)', data)
    print domain_name


def main():
    # find_all()
    find_domain_name()


if __name__ == '__main__':
    main()
