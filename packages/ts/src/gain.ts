/*
1024 * 1024 * 40
41943040
a = 1024 * 1024 * 40
41943040
a / 1024
40960
a / (1024 * 1024)
40
Math.log(a) / Math.log(1024)
2.5321928094887363
a = 1024 * 1024 * 1024 * 40
42949672960
Math.log(a) / Math.log(1024)
3.5321928094887363
a = 1024 * 1024 * 1024 * 4000000000
4294967296000000000
Math.log(a) / Math.log(1024)
6.189735285398626

"1024 * 1024 * 1024 * 4000000000"는 값이 아무리 커도 1024 로 몇번 곱하면 되는지 알 수 있다.

*/
export const formatBytes = (byteData: number) => {
  if (byteData === 0)
    return '0 Byte'
  const byte = 1024
  const sizes = ['Byte', 'KB', 'MB', 'GB', 'TB']
  const i = Math.floor(Math.log(byteData) / Math.log(byte))
  return `${Math.floor(byteData / byte ** i)} ${sizes[i]}`
}
