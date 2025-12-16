def calculate_profit_margin(revenue, cost):
    """
    Tyche Principle: Operations must yield >85% profit margin.
    """
    if cost == 0:
        return 100.0
    margin = ((revenue - cost) / revenue) * 100
    return margin

def audit_task_cost(task_name, estimated_cost):
    """
    Stop-Loss Protocol: Reject any task that requires credit card usage.
    """
    print(f"💰 Tyche Engine Auditing: {task_name}")
    
    # STRICT RULE: NO SPEND ALLOWED
    if estimated_cost > 0.00:
        return {
            "allowed": False, 
            "reason": "VIOLATION: Cost > $0.00. Free tools only."
        }
    
    return {
        "allowed": True, 
        "reason": "APPROVED: Zero Cost."
    }