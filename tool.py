def overlaps(partitions: dict[str,set[str]]) -> list[str]:
    names=sorted(partitions); out=[]
    for i,left in enumerate(names):
        for right in names[i+1:]:
            if partitions[left]&partitions[right]: out.append(f'{left}:{right}')
    return out
