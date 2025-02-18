from collections import deque

if __name__ == '__main__':
    T = 1

    for t in range(T):
        N, M = map(int, input().split())

        ARROWS = [[list(), list()] for _ in range(N)]
        # ARROWS[학생번호 - 1][0] = inbound list = nodes that are smaller than me
        # ARROWS[학생번호 - 1][1] = outbound list = nodes that are taller than me

        for i in range(M):
            a, b = map(int, input().split())
            ARROWS[a - 1][1].append(b - 1)
            ARROWS[b - 1][0].append(a - 1)

        answer = 0

        memos = [None for _ in range(N)]
        memot = [None for _ in range(N)]

        for i in range(N):
            sq = deque([i])
            sv = [False for _ in range(N)]
            scnt = 0
            sv[i] = True
            if memos[i] is not None:
                scnt = memos[i]
                sq.pop()

            while sq:
                n = sq.pop()

                for arrow in ARROWS[n][0]:
                    if not sv[arrow]:
                        sv[arrow] = True
                        sq.appendleft(arrow)
                        scnt += 1

            if memos[i] is None:
                memos[i] = scnt

            tq = deque([i])
            tv = [False for _ in range(N)]
            tcnt = 0
            tv[i] = True

            if memot[i] is not None:
                tcnt = memot[i]
                tq.pop()

            while tq:
                n = tq.pop()

                for arrow in ARROWS[n][1]:
                    if not tv[arrow]:
                        tv[arrow] = True
                        tq.appendleft(arrow)
                        tcnt += 1
            if memot[i] is None:
                memot[i] = tcnt


            if (tcnt + scnt + 1) == N:
                answer += 1

        print(answer)