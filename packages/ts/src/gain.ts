
export const formatBytes = (byteData: number) => {
  if (byteData === 0)
    return '0 Byte'
  const byte = 1024
  const sizes = ['Byte', 'KB', 'MB', 'GB', 'TB']
  const i = Math.floor(Math.log(byteData) / Math.log(byte))
  return `${Math.floor(byteData / byte ** i)} ${sizes[i]}`
}
