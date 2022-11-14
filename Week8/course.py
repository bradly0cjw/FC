def selectionsort(data,wall):
    if wall==len(data)-2:
        return
    else:
        m=min(data[wall:])
        idx=data.indecx(m,wall)
