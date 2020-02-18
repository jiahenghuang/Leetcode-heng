# 问题描述 给你一段英文或德文文字，你能编程识别它可能是哪种语言吗？研究发现，统计文字中字母“t”（或“T”）与“s”（或“S”）出现的次数，如果给定文字中“t”（或“T”）的出现次数比“s”（或“S”）多，则可能为英文，否则可能为德文。

# 问题输入
# 输入包括多个行数，首先给出整数N（1<N<10000），接着给出N行文字，每一行文字至少包括一个字符，至多100个字符。
# 问题输出
# 输出包括一行，如果输入文字可能为英文，则输出English，否则输出Deutsch。

# 示例
# 输入
# 6
# ON THIS THE REST OF THE ACHAEANS WITH
# ONE VOICE WERE FOR RESPECTING
# THE PRIEST AND TAKING THE RANSOM THAT HE OFFERED; BUT NOT SO AGAMEMNON,
# WHO SPOKE FIERCELY TO HIM AND SENT HIM ROUGHLY AWAY.
# OLD MAN, SAID HE,
# LET ME NOT FIND YOU TARRYING ABOUT OUR SHIPS
# 输出
# English