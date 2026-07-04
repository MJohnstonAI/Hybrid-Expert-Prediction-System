# Q&A GROUNDING AND TRUTH ANCHORING (qna_grounding.md)

*   **Q:** Can Matrix A generate duplicate numbers within a single prediction line?
    **A:** Absolute Failure Mode. The physical machine cannot drop duplicate balls. Output arrays must always contain 5 distinct, unique integers.
*   **Q:** How does the system handle an exact number repeat (stiction)?
    **A:** The system cross-references the historical index. If a number repeats across two consecutive draws (e.g., the 26 and 40 anomalies), its dynamic weight is capped to avoid chasing an infinite feedback loop.
*   **Q:** What is the geometric fulcrum of the bonus pool?
    **A:** **8.5**. Any calculation treating the bonus pool midpoint as 10.5 belongs to the deprecated 20-ball machine and must be rejected immediately.