class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        for a in asteroids:
            while st and a < 0 < st[-1]: #collision tbhi hota jb stack top + ho aur curr asteroid - ho
                if st[-1] < -a:
                    st.pop() # Stack top foot gaya, loop chalega
                    continue
                elif st[-1] == -a:
                    st.pop() # Both foot gaye
                break # Current asteroid destroy ho gaya
            else:
                st.append(a) # No collision
        return st
