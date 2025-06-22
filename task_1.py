time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
time_parts = time_str.split(',')
total_minutes = 0

for part in time_parts:
    components = part.split()
    part_minutes = 0
    
    for component in components:
        if 'h' in component:
            hours = int(component.replace('h', ''))
            part_minutes += hours * 60
        elif 'm' in component:
            minutes = int(component.replace('m', ''))
            part_minutes += minutes
        elif 's' in component:
            seconds = int(component.replace('s', ''))
            part_minutes += seconds // 60
    
    total_minutes += part_minutes

print(total_minutes)