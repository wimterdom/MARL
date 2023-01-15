echo "\033[31m [*] AFL environment setting... \033[0m"
echo "\033[33m [*] core pattern setting... \033[0m"
echo core >/proc/sys/kernel/core_pattern
echo "\033[33m [*] cpu scaling setting... \033[0m"
export AFL_SKIP_CPUFREQ=1
export AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1
echo "\033[32m [*] AFL environment setting finished! \033[0m"
