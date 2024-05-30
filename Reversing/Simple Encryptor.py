# HTB Simple Encryptor YS4B

import numpy as np
from ctypes import CDLL

"""

Using Ghidra, I found this script:

undefined8 main(void)

{
  int randomValue;
  time_t time;
  long in_FS_OFFSET;
  uint time_;
  uint randomValue2;
  long iterator;
  FILE *flag;
  size_t len_flag;
  void *flag_;
  FILE *Encripted_flag;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  flag = fopen("flag","rb");
  fseek(flag,0,2);
  len_flag = ftell(flag);
  fseek(flag,0,0);
  flag_ = malloc(len_flag);
  fread(flag_,len_flag,1,flag);
  fclose(flag);
  time = ::time((time_t *)0x0);
  time_ = (uint)time;
  srand(time_); (1) <-----
  for (iterator = 0; iterator < (long)len_flag; iterator = iterator + 1) {
    randomValue = rand();
    *(byte *)((long)flag_ + iterator) = *(byte *)((long)flag_ + iterator) ^ (byte)randomValue; (2) <-----
    randomValue2 = rand();
    randomValue2 = randomValue2 & 7;
    *(byte *)((long)flag_ + iterator) =
         *(byte *)((long)flag_ + iterator) << (sbyte)randomValue2 |
         *(byte *)((long)flag_ + iterator) >> 8 - (sbyte)randomValue2;(3) <-----
  }
  Encripted_flag = fopen("flag.enc","wb");
  fwrite(&time_,1,4,Encripted_flag); (4) <-----
  fwrite(flag_,1,len_flag,Encripted_flag); (5) <-----
  fclose(Encripted_flag);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

What interests us are parts (1), (2), (3), (4) and (5).

"""

libc = CDLL("libc.so.6")


flag_enc = open("flag.enc", "rb")
time = np.fromfile(flag_enc, dtype=np.uint32)[0]

libc.srand(int(time))

flag_enc = open("flag.enc", "rb")
content = np.fromfile(flag_enc, dtype=np.uint8)

Flag = ""

for i in range(4, len(content), 1):
    rand1 = libc.rand()
    rand2 = libc.rand()

    rand2 = rand2 & 7
    rand1 = rand1 & 255
    
    byte_ = (content[i] << (8 - rand2) | content[i] >> rand2)% 256

    byte_ = byte_ ^ rand1

    Flag += chr(byte_)

print(Flag) #HTB{vRy_s1MplE_F1LE3nCryp0r}
