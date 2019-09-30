cmake_minimum_required(VERSION 3.10)

add_executable(faktorial.bin faktorial.c)
add_executable(hviezdicky.bin hviezdicky.c)
add_executable(hviezdickyciselka.bin hviezdickyciselka.c)
add_executable(slova slova.c)

add_executable(nasobilka nasobilka.c)
target_link_libraries(nasobilka m)

add_executable(znamka_pat znamka_pat.c)