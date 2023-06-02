#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

template <typename T> // O(N)
bool linear_search(int N, std::vector<T> &seq)
{
    for (T i : seq)
    {
        if (i == N)
            return true;
    }
    return false;
}

template <typename T>
bool bin_search(int N, std::vector<T> &S)
{
    auto first = S.begin();
    auto last = S.end();

    while (true)
    {
        auto range_length = std::distance(first, last);
        auto mid_idx = first + std::floor(range_length / 2);
        auto mid_element = *(first + mid_idx);
        if (mid_element == N)
        {
            return true;
        }
        else if (mid_element > N)
        {
            // 반복자의 last가 -mid_idx 만큼 이동하쥬
            // 만약 N = 2이고 mid가 5면 5이상은 필요없다
            // 1234 중에 찾자
            std::advance(last, -mid_idx);
        }
        else if (mid_element < N)
        {
            std::advance(first, mid_idx)
        }

        if (range_length == 1)
            return false;
    }
}

void bin_search_test()
{
    int N = 3;
    std::vector<int> S{1, 3, 2, 4, 5, 6, 7, 8, 9, 10};
    std::sort(S.begin(), S.end());
    if (bin_search(N, S))
    {
        std::cout << "이진 검색으로 원소를 찾았다" << std::endl;
    }
}