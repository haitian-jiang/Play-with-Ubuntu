# 24-hour time format

The problem occurred when I start to use thunderbird calendar, as the calendar shows time in the format of 2 p.m., but I am familia with 14:00. So I try to find the setting of time format.

The problem cannot be solved within thunderbird setting, it is about the gnome setting for desktop applications. Run the following command can solve the problem.

```bash
gsettings set org.gnome.desktop.interface clock-format '24h'
```

[en reference](https://askubuntu.com/questions/214099/how-to-change-thunderbirds-display-time-to-24h-format)

[中文链接](https://qastack.cn/ubuntu/214099/how-to-change-thunderbirds-display-time-to-24h-format)
