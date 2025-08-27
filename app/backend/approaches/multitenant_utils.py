"""
multitenant_utils.py
Centralized multi-tenant enforcement for metadata filtering and access control.
"""
from typing import Any, Dict

def enforce_multitenant_access(context: Dict[str, Any], tenant_id: str) -> Dict[str, Any]:
    # Filter documents and responses by tenant_id
    documents = context.get('documents', [])
    filtered_docs = [doc for doc in documents if doc.get('tenant_id') == tenant_id]
    context['documents'] = filtered_docs
    return context

def enforce_response_access(response: Dict[str, Any], tenant_id: str) -> Dict[str, Any]:
    # Ensure response only contains data for the tenant
    if response.get('tenant_id') != tenant_id:
        return {}
    return response
