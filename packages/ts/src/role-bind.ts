interface RoleBinder {
  role: string; // role
  members: string[]; // user id list
}
interface ResourcePolicy {
  resource: string; //  posts/manualA, buckets/BucketA
  permission: string; // resource permission ex) post.owner, post.viewer, user.write
  bindings: RoleBinder[];
}
// 접근한 페이지(리소스)에서 요구하는 스펙
interface RequestPolicyEval {
  resource: string;
  permission: string; // requiredPermission
  member: string; // 유저의 권한 목록
}
const roleAdmin: RoleBinder = {
  role: 'admin',
  members: ['adminA@gmail.com'],
};
const roleWorker: RoleBinder = {
  role: 'manual.viewer',
  members: ['worker@gmail.com'],
};
const bindings: RoleBinder[] = [roleAdmin, roleWorker];
const manualAViewPolicy: ResourcePolicy = {
  resource: 'posts/manualA',
  permission: 'post.viewer',
  bindings,
};

const manualAOwnerPolicy: ResourcePolicy = {
  resource: 'posts/manualA',
  permission: 'post.viewer',
  bindings,
};
const policyList = [manualAViewPolicy, manualAOwnerPolicy];

function evaluatePolicy(rp: RequestPolicyEval) {
  // 리소스에 속한 정책들을 가져온다
  const resPolicies = policyList.filter(
    p => p.resource === rp.resource && p.permission === rp.permission
  );
  if (resPolicies.length < 1)
    throw new Error(`${rp.resource}-${rp.permission}에 대한 정책이 없습니다.`);
  // 리소스 정책에 속한 권한과 유저의 권한을 비교한다
  let passed = false;
  for (let i = 0; i < resPolicies.length; i++) {
    const resPolicy = resPolicies[i];
    for (let j = 0; j < resPolicy.bindings.length; j++) {
      const bind = resPolicy.bindings[j];
      for (let z = 0; z < bind.members.length; z++) {
        const member = bind.members[z];
        if (member === rp.member) {
          passed = true;
          break;
        }
      }
      if (passed) break;
    }
    if (passed) break;
  }
}
// binding 확인 시나리오
// resource1 의 ResourcePolicy 확인

// 유저 시나리오
// 1. 유저 worker@gmail.com 가 resource1.read 권한 평가질의
// 2. resource1 정책에 속한 bindings를 확인, 불통과
// 3. parent resource 정책에 속한 bindings를 확인, 통과
