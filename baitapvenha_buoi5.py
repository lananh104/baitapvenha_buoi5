#  BÀI TẬP VỀ NHÀ BUỔI 05 - Tuple:
# Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
#     Sau đó, unpack các phần tử trong một tuple.
# Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
# Bài 02: Viết chương trình đảo ngược một tuple.
# Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
# Bài 04: Cho 1 list chứa các tuple không rỗng.
#     Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
#     Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
# Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
# Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
# Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.



###Làm các ví dụ
a={1,2,3}
b={3,4,5,6,7,8}
###  Các phương thức của Set:
#     - set.add(element): Thêm một phần tử element vào set
a.add(4)
print(a)
#     - set.clear(): Xóa toàn bộ các phần tử của set thành set rỗng
a.clear()
print(a)
#     - set.copy(): Trả lại một bản sao của set
c=a.copy()
print(c)
#     - set.difference(*other_set): Trả lại một set là phần bù của 2 hoặc nhiều set
x=a.difference(b)
y=b.difference(a)
print(x)
print(y)
#     - set.difference_update(other_set): Cập nhật lại set bằng các giá trị phần bù của set với other_set (nếu có)
print(a.difference_update(b))
#     - set.discard(element): Xóa một phần tử element trong set (ko làm gì nếu như element ko tồn tại trong set)
a.discard(3)
print(a)
#     - set.intersection(*other_set): Trả lại giao của 2 hoặc nhiều set
x=a&b
y=a.intersection(b)
z=b.intersection(a)
print(x)
print(z)
print(y)
#     - set.intersection_update(other_set): Cập nhật lại set bằng các giá trị giao giữa nó và other_set
print(a.intersection_update(b))
#     - set.isdisjoint(other_set): Trả lại True nếu set và other_set không giao nhau
print(a.isdisjoint(b))
#     - set.issubset(other_set): Trả lại True nếu set là con của other_set
print(a.issubset(b))
#     - set.issuperset(other_set): Trả lại True nếu set có chứa other_set
print(a.issuperset(b))
#     - set.pop(): Xóa và trả lại một phần tử ngẫu nhiên trong set. Trả lại KeyError nếu như set rỗng
a.pop()
print(a)
#     - set.remove(elemet): Xóa element khỏi set, nếu element không tồn tại sẽ báo lỗi KeyError
a.remove(3)
print(a)
#     - set.symmetric_difference(*other_set): Trả lại phần bù đối xứng của 2 hoặc nhiều set
c=a.symmetric_difference(b)
print(c)
#     - set.symmetric_difference_update(other_set): Cập nhật lại set bằng các giá trị phần bù đối xứng giữa nó và other_set
print(a.symmetric_difference_update(b))
#     - set.union(*other_set): Trả lại hợp giữa 2 hoặc nhiều set
x=a&b
y=a.union(b)
print(x)
print(y)
#     - set.update(other_set): Cập nhật set bằng hợp giữa nó và other_set
a.update(b)
print(a)
### Các hàm dựng sẵn với Set (List và cả các kiểu dữ liệu có thể iterable):
#     - all(): Trả lại True nếu như tất cả các phần tử là True hoặc nó rỗng
print(all(a))
#     - any(): Trả lại True nếu như bất kì phần tử nào đó là True, trong trường hợp rỗng thì return False
print(any(a))
#     - enumerate(): Trả lại một đối tượng kiểu enumerate (liệt kê). Nó chứa các cặp gồm chỉ số và giá trị tương ứng
#     - len(): Trả lại số lượng phần tử
print(len(a))
#     - max(): Trả lại giá trị lớn nhất
print(max(a))
#     - min(): Trả lại giá trị nhỏ nhất
print(min(a))
#     - sorted(): Sắp xếp các phần tử trả lại giá trị ra, ko tác động lên biến gốc
print(sorted(a))
#     - sum(): Trả lại tổng các phần tử
print(sum(a))




# Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
#     Sau đó, unpack các phần tử trong một tuple.
a=("a",1,(1,2,3),[1,2],{1,2,2},"")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])


# Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
a=(1,2)
b=[1,2]
c=[a]
d=(a)
print(type(c))
print(type(d))


# Bài 02: Viết chương trình đảo ngược một tuple.
a=(input("Mời nhập một Tuple: "))
print(a[::-1])


# Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
a=[1,2,(1,2),1]
n=0
for i in range(len(a)):
    if type(a[i])==tuple:
        n=i
        break
    else:
        n=len(a)
print("số lượng các phần tử câng tìm là: ",n)


# Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
a=[(1,2),(1,5),(1,3,2),(4,3,5),(0,7)]
min=a[0][1]
for i in range(len(a)):
    if a[i][1]<min:
        min=a[i][1]
        print(a[i])
    else:
        print(a[0])
        break


# Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
while True:
    a=(1,2,3,4,5)
    print(type(a))
    if len(a)<4:
        print("Tuple trên có ít hơn 4 phần tử. Mời nhập lại!")
    else:
        print("Phần tử thứ 4 của Tuple trên là: ",a[3])
        print("Phần tử thứ 4 từ dưới lên của Tuple trên là: ",a[-4])
    break


# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
# Cách 1: dùng for lồng nhau:
a=(1,2,3,4,5)
b=(6,7,8,9,10,2,3)
test=0
for i in a:
    for j in b:
        if i==j:
           test=1
if test==0:
    print("2 Tuple không có phần tử nào chung")
else:
    print("2 Tuple có phần tử chung")

# Cách 2: dùng set{}
a=(1,2,3,4,5)
b=(6,7,8,9,10,2,3)
c=set(a)
d=set(b)
i=c&d
if len(i)==0:
    print("2 Tuple không có phần tử nào chung")
else:
    print("2 Tuple có {} phần tử chung đó là {} ".format(len(i),i))


# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
# Cách 1:Dùng a.count(i)
a=(1,1,1,2,1,1,1)
for i in a:
    if a.count(i)==len(a):
        print("Tất cả các phần tử trong tuple giống nhau")
    else:
        print("Tuple gồm các phần tử khác nhau")
    break

# Cách 2: dùng set{}
a=(1,1,1,2,1,1,1)
b=set(a)
if len(b)==1:
    print("Tất cả các phần tử trong tuple giống nhau")
else:
    print("Tuple gồm {} phần tử {} ".format(len(b),b))


# Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
import math
a=(math.pi,math.e,1.5)
print("Tổng các giá trị trong Tuple là: ",round(sum(a),2))
print("Giá trị lớn nhất trong Tuple trên là: ",max(a))


# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
a=["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
b=[]
for i in a:
    c=i.split(".")
    b.append(c[-1])
print(b)


# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
a=(input("Mời nhập câu tùy ý: "))
b=a.split(" ")
print("Từ dài nhất trong câu là: ",max(b,key=len))














