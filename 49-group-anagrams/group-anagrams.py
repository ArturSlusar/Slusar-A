class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Используем defaultdict для автоматического создания списков значений
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # Сортируем символы слова и преобразуем в кортеж (неизменяемый тип для ключа)
            sorted_word = tuple(sorted(word))
            
            # Группируем исходное слово по его отсортированному ключу
            anagrams[sorted_word].append(word)
            
        return list(anagrams.values())
        