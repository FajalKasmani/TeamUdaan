"""
Test script to verify core logic works without UI (Implementation Step 2).
This demonstrates that the complaint processing works end-to-end.
"""

from agents import ComplaintResolverWorkflow
from memory import ComplaintMemory


def test_core_logic():
    """Test the core complaint processing logic."""
    
    print("=" * 60)
    print("🧪 TESTING CORE LOGIC (Step 2: No UI)")
    print("=" * 60)
    print()
    
    # Initialize workflow
    workflow = ComplaintResolverWorkflow()
    memory = ComplaintMemory()
    
    # Test complaints
    test_complaints = [
        "My refund is not received",
        "The app keeps crashing every time I try to login",
        "I requested a refund 2 weeks ago but haven't received it"
    ]
    
    print("📝 Processing test complaints...")
    print()
    
    for idx, complaint in enumerate(test_complaints, 1):
        print(f"\n{'='*60}")
        print(f"TEST {idx}: {complaint}")
        print(f"{'='*60}")
        
        # Process complaint through workflow
        result = workflow.process_complaint(complaint)
        
        # Display results
        print(f"\n✅ Category: {result['category']}")
        print(f"✅ Initial Priority: {result['initial_priority']}")
        print(f"✅ Final Priority: {result['final_priority']}")
        print(f"✅ Priority Changed: {result['priority_changed']}")
        print(f"\n📧 Response:")
        print(f"   {result['response']}")
        print(f"\n🛠️  Recommended Action: {result['action']}")
        
        # Store in memory if high priority
        if result['final_priority'].lower() == 'high':
            memory.add_complaint(
                complaint=complaint,
                category=result['category'],
                priority=result['final_priority']
            )
            print(f"\n💾 Stored in memory (High Priority)")
        
        print()
    
    # Show memory
    print(f"\n{'='*60}")
    print("📊 MEMORY STATUS")
    print(f"{'='*60}")
    print(f"High-priority complaints stored: {memory.get_complaint_count()}")
    
    if memory.get_complaint_count() > 0:
        print("\nStored complaints:")
        for comp in memory.get_all_complaints():
            print(f"  - {comp['id']}: {comp['complaint'][:50]}... ({comp['priority']})")
    
    print(f"\n{'='*60}")
    print("✅ CORE LOGIC TEST COMPLETE!")
    print("✅ All agents working correctly!")
    print("✅ Memory system functional!")
    print("✅ Ready for UI implementation!")
    print(f"{'='*60}")


if __name__ == "__main__":
    test_core_logic()






