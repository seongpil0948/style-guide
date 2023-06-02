#include <chrono>

std::chrono::steady_clock::time_point begin_or_end()
{
    return std::chrono::steady_clock::now();
}
using m_sec = std::chrono::microseconds;

m_sec diff_time(m_sec end, m_sec begin)
{
    return std::chrono::duration_cast<m_sec>(end - begin);
}
