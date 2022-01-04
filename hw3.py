# problem 3
def neighbor_sum(a_list):
    n = len(a_list)
    # create a new list where the neighbors of each element are added to it
    b_list = [0 for i in range(n)]
    for i in range(0, n):
        # when there's number on the leftside
        if i - 1 >= 0:  
            b_list[i] += a_list[i - 1]
        # when there's number on the rightside  
        if i + 1 < n:  
            b_list[i] += a_list[i + 1]
        # add itself all the time  
        b_list[i] += a_list[i]   
    return b_list


# problem 4
def cal(e):
    # all the tax rate
    taxRate = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    # all thresholds corresponded with the tax rate
    Single = [0.0, 9950.0, 40525.0, 86375.0, 164925.0, 209425.0, 5236600.0]
    n = len(e)
    total = [0 for i in range(n)]

    for j in range(n):  
        # for adding paid tax in every range
        add_paid = 0.0   
        # in 2021, income $12550 is tax free
        if e[j] <= 12550:
            continue
        # start to calculate income part which need be taxed
        e[j] -= 12550
        # go through 7 tax rate ranges
        for i in range(7):
            # when supposed tax part is less or equal to 0, meaning no income part need to be taxed
            if e[j] <= 0:
                break
            if i != 6:
                # the most supposed tax pay from current tax range
                diff = Single[i + 1] - Single[i]
                # how much income is supposed to be calculated from current tax rate range
                be_taxed = min(diff, e[j])
                # in case it will come negative numbers for complete logic, although it seems unnecessary
                be_taxed = max(0, be_taxed)
                # calculate how much tax should be paid from current range
                add_paid += taxRate[i] * be_taxed
                # remove already taxed income part from total income
                e[j] -= be_taxed
            else:
                # when income over $523601
                be_taxed = e[j]
                be_taxed = max(0, be_taxed)
                add_paid += taxRate[i] * be_taxed
        total[j] = add_paid
    return total


def get_income_tax(e):
    return cal(e)


# problem 5
class SetSuite:
    
    def __init__(self, list_of_lists):
        self._list = []
        for a_list in list_of_lists:
            self.add_set(a_list)

    # adds a new set to the internal list of sets
    def add_set(self, new_List):
        self._list.append(list(set(new_List)))

    # returns the internal list of sets
    def get_sets(self):
        return self._list

    # returns the union set of all sets
    def union_all(self):
        u_set = set()
        for a_set in self._list:
            u_set = u_set.union(set(a_set))
        return list(u_set)

    # returns the intersection set of all sets
    def intersection_all(self):
        if len(self._list) == 0:
            return list(set())

        i_set = set(self._list[0])
        for a_set in self._list[1:]:
            i_set = i_set.intersection(a_set)
        return list(i_set)




# problem 6
def pascal(row):
    # pattern as below
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1
    # every number is the sum of upper one and left upper number, no existence is 0
    tri = [[0 for i in range(row + 10)] for i in range(row + 10)]
    tri[0][0] = 1
    for i in range(1, row + 1):
        tri[i][0] = 1
        for j in range(1, row + 1):
            tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
    return tri[row][:row + 1]


# problem 7
def perfect_power(num_1, num_2):
    power_num = num_1
    # corner case
    if num_1 == num_2:
        return True
    # keep multiple num_1 until they are equal
    while num_1 < num_2:
        num_1 *= power_num
        if num_1 == num_2:
            return True
    return False


# extra credit

def change(num, l, r, base, cur):
    # left and right are the range of num, cur is some power of base
    if l > r:
        return 0
    # turn the last digit of num into integer
    e = int(num[r])
    # value of current position multiple cur, then add value from left to (right-1) of num
    return cur * e + change(num, l, r - 1, base, cur * base)


def convert_to_10(num, base):
    l = 0
    r = len(num) - 1
    for i in range(r + 1):
        if int(num[i]) >= base:
            return "Invalid Number"
    return change(num, l, r, base, 1)
