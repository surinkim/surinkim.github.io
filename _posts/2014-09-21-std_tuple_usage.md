---
layout: post
title: std::tuple
---

c++11에 포함된 std::tuple은 개념상으로는 POD(Plain old data) 를 가지는 struct와 유사하지만, struct가 이름으로 멤버에 접근하는 대신 tuple의 멤버들은 tuple내의 순서로 접근한다.

{% highlight C++ linenos %}
//struct exmaple
struct ExampleST
{
    int     id_;
    string  name_;
 
}example_st = {1, "john"};
 
cout << "id = " << example_st.id_ << endl;
cout << "name = " << example_st.name_ << endl;
 
//tuple example
enum {ID, NAME};
std::tuple<int, string> example_tu(2, "suzi");
cout << "id = " << std::get<0>(example_tu) << endl;
cout << "name = " << std::get<1>(example_tu) << endl;
{% endhighlight %}

std::tie는 tuple object를 unpacking 할 때 사용된다. 그러니까 tie의 인자로 받는 변수에 tuple 오브젝트 내의 데이터를 순서대로 '묶어준다.' 이때, tuple내의 특정 데이터를 묶을 필요가 없다면 std::ignore 상수를 사용한다.

{% highlight C++ linenos %}
int id;
std::tie(id, std::ignore) = example_tu;
cout << "tied id = " << id << endl;
{% endhighlight %}

std::tie를 쓰면 아래처럼 swap처리를 간단히 할 수 있다.
{% highlight C++ linenos %}
//보통의 swap 처리
int a = 3, z = 4;
int temp = a;
a = z;
z = temp;
 
//std::tie를 사용한 swap 처리
a = 3, z = 4;
std::tie(z, a) = std::make_tuple(a, z);
{% endhighlight %}

그리고, sort의 기준이 여러 개일때, tuple의 진가가 발휘된다. 아래와 같은 배열을 정렬하는데, 첫번째 값이 동일하면 두번째 값을, 두번째 값이 동일하면 세번째 값을 비교하는 식으로 정렬한다고 해보자. 보통은 operator >나 operater <를 정의하고, 내부에서는 if else를 써야 할 것이다. 아래 코드는 이것을 간결하게 처리한다.  

{% highlight C++ linenos %}
struct ArrayNums
{
    int num[3];
}array_nums[] =
{
    {1000, 2000, 3000},
    {1001, 2002, 3003},
    {1001, 2001, 3001},
    {1001, 2002, 3002},
};
 
cout << "<before sorting>" << endl;
for_each(begin(array_nums), end(array_nums), [&](const ArrayNums& array)
{
    cout << array.num[0] << ", " << array.num[1] << ", " << array.num[2] << endl;
 
});
 
//오름차순 sorting에 사용할 lambda func
auto array_less = [](ArrayNums& a, ArrayNums& b) -> bool
{
    return (tie(a.num[0], a.num[1], a.num[2]) < tie(b.num[0], b.num[1], b.num[2]));
};
 
//sorting
std::sort(begin(array_nums), end(array_nums), array_less);
 
cout << endl << "<after sorting>" << endl;
for_each(begin(array_nums), end(array_nums), [&](const ArrayNums& array)
{
    cout << array.num[0] << ", " << array.num[1] << ", " << array.num[2] << endl;
 
});
{% endhighlight %}

