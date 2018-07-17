; Q1
(define (sign x)
  (cond
      ((> x 0) 1)
      ((= x 0) 0)
      ((< x 0) -1)
  )
)

; Q2
(define (square x) (* x x))

(define (pow b n)
  (cond
    ((zero? n) 1)
    ((even? n) (square (pow b (/ n 2))))
    ((odd? n) (* b (square (pow b (/ (- n 1) 2))))
)))

; Q3
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

; Q4
(define (ordered? s)
  (cond
    ((null? s) #t)
    ((null? (cdr s)) #t)
    ((>= (car (cdr s)) (car s)) (ordered? (cdr s)))
    (else #f)
  )
)

; Q5
(define (nodots s)
  (if (null? s) nil
  (if (integer? s) (cons s nil)
  (if (pair? (car s))(cons (nodots (car s)) (nodots (cdr s )))
  (if (integer? (cdr s))(cons (car s ) (cons (cdr s) nil))(cons (car s) (nodots (cdr s))))))))

; Q6
(define (empty? s) (null? s))

(define (add s v)
    (cond ((empty? s) (list v))
    ((equal? (car s) v) s)
    (( > (car s) v) (cons v s))
    (else (cons (car s) (add (cdr s) v)))
    )
)

; Q7
; Sets as sorted lists
(define (contains? s v)
  (cond
    ((equal? s nil) #f)
    ((equal? (car s) v) #t)
    (else (contains? (cdr s) v))
    )
)

; Q8
(define (intersect s t)
    (cond
      ((empty? s) nil)
      ((empty? t) nil)
      ((< (car s) (car t)) (intersect (cdr s) t))
      ((> (car s) (car t)) (intersect (cdr t) s))
      ((= (car s) (car t)) (cons (car s)(intersect (cdr s) (cdr t))))
    )
)


(define (union s t)
    (cond
      ((empty? s) t)
      ((empty? t) s)
      ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
      ((> (car s) (car t)) (cons (car t) (union (cdr t) s)))
      ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
    )
)
